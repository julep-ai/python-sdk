# type: ignore
import inspect
from functools import wraps
from typing_extensions import ParamSpec

from .. import resources

P = ParamSpec("P")


def patch_extra_body(cls, method: str, named_args: list[str] = []):
    # Step 1: Retrieve the original start function
    original_method = getattr(cls, method)

    # Step 2: Analyze the original function's signature
    signature = inspect.signature(original_method)
    params = signature.parameters

    # Extract the names of the keyword-only parameters
    keyword_only_params = [name for name, param in params.items() if param.kind == inspect.Parameter.KEYWORD_ONLY]

    # Define which parameters are allowed as keyword arguments
    allowed_kwargs = set(keyword_only_params).union(named_args)

    # Step 3: Define the wrapper function
    @wraps(original_method)
    def patched_method(*args: P.args, **kwargs: P.kwargs):
        # Bind the arguments to the original function's signature
        try:
            bound_args = signature.bind(*args, **{k: v for k, v in kwargs.items() if k in allowed_kwargs})
        except TypeError as e:
            # Handle missing required arguments or other signature mismatches
            raise TypeError(f"Error calling {method}: {e}") from e

        bound_args.apply_defaults()

        # Separate extra keyword arguments
        extra_kwargs = {k: v for k, v in kwargs.items() if k not in allowed_kwargs and k not in params}

        # If there are extra keyword arguments, merge them into 'extra_body'
        if extra_kwargs:
            if "extra_body" in bound_args.arguments and isinstance(bound_args.arguments["extra_body"], dict):
                # Merge existing extra_body with extra_kwargs
                bound_args.arguments["extra_body"] = {**bound_args.arguments["extra_body"], **extra_kwargs}
            else:
                # If extra_body is not provided, create it with extra_kwargs
                bound_args.arguments["extra_body"] = extra_kwargs

        # Call the original start function with modified arguments
        return original_method(*bound_args.args, **bound_args.kwargs)

    # Step 4: Monkeypatch the start function
    setattr(cls, method, patched_method)


def setup():
    patch_extra_body(resources.tasks.TasksResource, "create", ["agent_id"])
    patch_extra_body(resources.tasks.TasksResource, "create_or_update", ["task_id"])


def check():
    setup()
    from .. import Client

    client = Client()

    [agent, *_] = client.agents.list()

    task = client.tasks.create_or_update(
        agent_id=agent.id,
        task_id=agent.id,
        name="test",
        description="test",
        main=[{"evaluate": {"_": "'hello'"}}],
        subworkflow=[{"evaluate": {"_": "'hello'"}}],
    )
