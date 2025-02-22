import inspect
from typing import Callable, Dict, List, Set, Union

from ..typing import T_Dispatcher
from .decorator import Decorator


class ExecTarget:
    callable: Callable
    inline_dispatchers: List[T_Dispatcher]
    decorators: List[Decorator]

    param_paths: Dict[str, List[T_Dispatcher]]

    def __init__(
        self,
        callable: Callable,
        inline_dispatchers: List[T_Dispatcher] = None,
        decorators: List[Decorator] = None,
    ):
        self.callable = callable
        self.inline_dispatchers = inline_dispatchers or []
        self.decorators = decorators or []

        self.param_paths = {}
