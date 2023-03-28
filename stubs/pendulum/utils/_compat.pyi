from collections.abc import Iterable
from typing import Final

PY2: Final[bool]
PY36: Final[bool]
PYPY: Final[bool]

def decode(string: bytes, encodings: Iterable[str] = ...) -> str: ...
def encode(string: str, encodings: Iterable[str] = ...) -> bytes: ...
