from typing import Any, Protocol

class _FluentFunction(Protocol):
    def __call__(self, input: Any, /, **kwargs: Any) -> Any: ...

NUMBER: _FluentFunction = ...
DATETIME: _FluentFunction = ...
BUILTINS: dict[str, _FluentFunction] = ...