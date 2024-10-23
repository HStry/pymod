"patches to builtin objects"

__all__ = ['UNSET', 'isinstance', 'sources']

from collections.abc import Collection
from typing import Optional, Union, Any
from builtins import isinstance as _isinstance
import inspect

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

def sources(*objects, **kwobjects):
    "Prints the sources of provided objects."
    keylength = max(0, len(str(len(objects))), *(len(str(k)) for k in kwobjects))
    iobjects = ((f"{i:>{keylength}d}", o) for (i, o) in enumerate(objects))
    
    for key, obj in *iobjects, *kwobjects.items():
        try:
            name = f"{key} ({obj.__name__})"
        except AttributeError:
            name = f"{key}"
        
        print(f"# {name}:")
        try:
            print(inspect.getsource(obj))
        except (TypeError, ValueError):
            print("#    <unable to retrieve source>")
