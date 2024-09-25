from collections.abc import Collection
from typing import Optional, Union, Any
from builtins import isinstance as __isinstance
from ._common import UNSET

T = Union[type, Collection[type, ...]]
UT = Union[UNSET, type, Collection[type, ...]]

def isinstance(obj: Any, types: T, antitypes: UT = UNSET):
    if antitypes is UNSET:
        return __isinstance(obj, types)
    return (__isinstance(obj, types)
            and not __isinstance(obj, antitypes))
