try:
    from .exceptions import *  # NOQA: F403
    from .routing import MATCH_ALL, Route
    from .errors import *  # NOQA: F403
    from .view import LonaView
    from .app import LonaApp

except ImportError as e:
    # this can happen while installing the package and can be ignored
    if e.name != 'typing_extensions':
        raise

VERSION = (1, 8, 5)
VERSION_STRING = '.'.join(str(i) for i in VERSION)
