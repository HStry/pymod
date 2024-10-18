"patches to builtin objects"

__all__ = ['UNSET', 'isinstance']

from collections.abc import Collection
from typing import Optional, Union, Any
from builtins import isinstance as _isinstance

class UNSET(object):
    def __new__(cls):
        try:
            return cls._unset
        except AttributeError:
            cls._unset = super().__new__(cls)
            return cls._unset
    
    def __bool__(self):
        return False
    
    def __repr__(self):
        return "<{self.__class__.__name__}>"

UNSET = UNSET()

T = Union[type, Collection[type, ...]]
UT = Union[UNSET, type, Collection[type, ...]]

def isinstance(obj: Any, types: T, antitypes: UT = UNSET):
    if antitypes is UNSET:
        return _isinstance(obj, types)
    return (_isinstance(obj, types)
            and not _isinstance(obj, antitypes))
