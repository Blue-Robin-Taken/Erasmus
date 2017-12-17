# Stubs for asyncpg.connect_utils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple

_ConnectionParameters = namedtuple('ConnectionParameters', ['user', 'password', 'database', 'ssl', 'connect_timeout', 'server_settings'])

_ClientConfiguration = namedtuple('ConnectionConfiguration', ['command_timeout', 'statement_cache_size', 'max_cached_statement_lifetime', 'max_cacheable_statement_size'])
