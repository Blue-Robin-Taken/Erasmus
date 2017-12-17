# Stubs for asyncpg.transaction (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import enum
from typing import Any, AsyncContextManager

class TransactionState(enum.Enum):
    NEW: int = ...
    STARTED: int = ...
    COMMITTED: int = ...
    ROLLEDBACK: int = ...
    FAILED: int = ...

ISOLATION_LEVELS: Any

class Transaction(AsyncContextManager[None]):
    def __init__(self, connection, isolation, readonly, deferrable) -> None: ...
    async def start(self) -> None: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
