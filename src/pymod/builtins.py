"patches to builtin objects"

__all__ = ['isinstance']

from collections.abc import Collection
from typing import Optional, Union, Any
from builtins import isinstance as _isinstance
from ._common import UNSET

T = Union[type, Collection[type, ...]]
UT = Union[UNSET, type, Collection[type, ...]]

def isinstance(obj: Any, types: T, antitypes: UT = UNSET):
    if antitypes is UNSET:
        return _isinstance(obj, types)
    return (_isinstance(obj, types)
            and not _isinstance(obj, antitypes))
