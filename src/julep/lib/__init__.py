# type: ignore
import inspect
from typing import Callable
from functools import wraps
from typing_extensions import ParamSpec

from .. import resources

P = ParamSpec("P")

orig_create = resources.tasks.TasksResource.create
orig_create_or_update = resources.tasks.TasksResource.create_or_update
create_spec = inspect.getfullargspec(resources.tasks.TasksResource.create)
create_or_update_spec = inspect.getfullargspec(resources.tasks.TasksResource.create_or_update)


def make_patch(kw: "list[str]", method: Callable, positional_args: list[str] = []):
    @wraps(method)
    def patched_method(self: resources.tasks.TasksResource, *args: P.args, **kwargs: P.kwargs):
        args += tuple([kwarg for arg in positional_args if (kwarg := kwargs.pop(arg, None))])
        
        extra_args = set(kwargs.keys()).difference(set(kw))
        
        if extra_args:
            extra_body = {k: kwargs.pop(k) for k in extra_args}
            kwargs["extra_body"] = extra_body
        return method(self, *args, **kwargs)

    return patched_method


def setup():
    resources.tasks.TasksResource.create = make_patch(create_spec.kwonlyargs, orig_create, positional_args=["agent_id"])
    resources.tasks.TasksResource.create_or_update = make_patch(
        create_or_update_spec.kwonlyargs, orig_create_or_update, positional_args=["task_id"]
    )
