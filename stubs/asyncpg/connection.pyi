# Stubs for asyncpg.connection (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import connect_utils
from .exceptions import PostgresLogMessage
from .types import ServerVersion
from .protocol import Record
from .protocol.protocol import ConnectionSettings
from .cursor import CursorFactory
from .prepared_stmt import PreparedStatement
from .transaction import Transaction
from collections import namedtuple
from typing import (
    Any, Optional, Union, Type, TypeVar, overload, Callable, List, Iterable, Sequence, IO, Awaitable,
    AsyncIterable
)
from os import PathLike
from asyncio import AbstractEventLoop
from ssl import SSLContext

class ConnectionMeta(type):
    def __instancecheck__(cls, instance): ...

class Connection:
    def __init__(self, protocol: Any, transport: Any, loop: Any, addr: Any, config: connect_utils._ClientConfiguration,
                 params: connect_utils._ConnectionParameters) -> None: ...
    async def add_listener(self, channel: str, callback: Callable[['Connection', int, str, Any], Any]) -> None: ...
    async def remove_listener(self, channel: str, callback: Callable[['Connection', int, str, Any], Any]) -> None: ...
    def add_log_listener(self, callback: Callable[['Connection', PostgresLogMessage], Any]) -> None: ...
    def remove_log_listener(self, callback: Callable[['Connection', PostgresLogMessage], Any]) -> None: ...
    def get_server_pid(self) -> int: ...
    def get_server_version(self) -> ServerVersion: ...
    def get_settings(self) -> ConnectionSettings: ...
    def transaction(self, *, isolation: str = ..., readonly: bool = ..., deferrable: bool = ...) -> Transaction: ...
    async def execute(self, query: str, *args, timeout: float = ...) -> str: ...
    async def executemany(self, command: str, args: Iterable[Sequence[Any]], *, timeout: float = ...) -> None: ...
    def cursor(self, query: str, *args, prefetch: int = ..., timeout: float = ...) -> CursorFactory: ...
    async def prepare(self, query: str, *, timeout: float = ...) -> PreparedStatement: ...
    async def fetch(self, query: str, *args, timeout: float = ...) -> List[Record]: ...
    async def fetchval(self, query: str, *args, column: int = ..., timeout: float = ...) -> Optional[Any]: ...
    async def fetchrow(self, query: str, *args, timeout: float = ...) -> Optional[Record]: ...
    async def copy_from_table(self, table_name: str, *, output: Union[PathLike, IO, Callable[[bytes], Awaitable[Any]]],
                              columns: List[str] = ..., schema_name: str = ..., timeout: float = ...,
                              format: Optional[Any] = ..., oids: Optional[Any] = ..., delimiter: Optional[Any] = ...,
                              null: Optional[Any] = ..., header: Optional[Any] = ..., quote: Optional[Any] = ...,
                              escape: Optional[Any] = ..., force_quote: Optional[Any] = ...,
                              encoding: Optional[Any] = ...) -> str: ...
    async def copy_from_query(self, query: str, *args, output: Union[PathLike, IO, Callable[[bytes], Awaitable[Any]]],
                              timeout: float = ..., format: Optional[Any] = ...,
                              oids: Optional[Any] = ..., delimiter: Optional[Any] = ..., null: Optional[Any] = ...,
                              header: Optional[Any] = ..., quote: Optional[Any] = ..., escape: Optional[Any] = ...,
                              force_quote: Optional[Any] = ..., encoding: Optional[Any] = ...) -> str: ...
    async def copy_to_table(self, table_name: str, *, source: Union[PathLike, IO, AsyncIterable[bytes]],
                            columns: List[str] = ..., schema_name: str = ...,
                            timeout: float = ..., format: Optional[Any] = ..., oids: Optional[Any] = ...,
                            freeze: Optional[Any] = ..., delimiter: Optional[Any] = ..., null: Optional[Any] = ...,
                            header: Optional[Any] = ..., quote: Optional[Any] = ..., escape: Optional[Any] = ...,
                            force_quote: Optional[Any] = ..., force_not_null: Optional[Any] = ...,
                            force_null: Optional[Any] = ..., encoding: Optional[Any] = ...) -> str: ...
    async def copy_records_to_table(self, table_name: str, *, records: Iterable[tuple], columns: List[str] = ...,
                                    schema_name: str = ..., timeout: float = ...) -> str: ...
    async def set_type_codec(self, typename: str, *, schema: str = ..., encoder: Any, decoder: Any,
                             binary: Optional[Any] = ..., format: str = ...) -> None: ...
    async def reset_type_codec(self, typename: str, *, schema: str = ...) -> None: ...
    async def set_builtin_type_codec(self, typename: str, *, schema: str = ..., codec_name: str) -> None: ...
    def is_closed(self) -> bool: ...
    async def close(self) -> None: ...
    def terminate(self) -> None: ...
    async def reset(self) -> None: ...


_CT = TypeVar('_CT', bound=Connection)


def connect(dsn: Optional[str] = ..., *, host: Optional[str] = ..., port: Optional[int] = ...,
            user: Optional[str] = ..., password: Optional[str] = ..., database: Optional[str] = ...,
            loop: Optional[AbstractEventLoop] = ..., timeout: int = ..., statement_cache_size: int = ...,
            max_cached_statement_lifetime: int = ..., max_cacheable_statement_size: int = ...,
            command_timeout: Optional[int] = ..., ssl: Optional[Union[bool, SSLContext]] = ...,
            connection_class: Type[_CT] = ..., server_settings: Optional[Any] = ...) -> _CT: ...

class _StatementCacheEntry:
    def __init__(self, cache, query, statement) -> None: ...

class _StatementCache:
    def __init__(self, loop, max_size, on_remove, max_lifetime) -> None: ...
    def __len__(self): ...
    def get_max_size(self): ...
    def set_max_size(self, new_size): ...
    def get_max_lifetime(self): ...
    def set_max_lifetime(self, new_lifetime): ...
    def get(self, query, *, promote: bool = ...): ...
    def has(self, query): ...
    def put(self, query, statement): ...
    def iter_statements(self): ...
    def clear(self): ...

class _Atomic:
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, t, e, tb): ...

class _ConnectionProxy: ...

ServerCapabilities = namedtuple('ServerCapabilities', ['advisory_locks', 'notifications', 'plpgsql', 'sql_reset', 'sql_close_all'])
