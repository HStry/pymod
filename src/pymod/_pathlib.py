"pathlib patches"

__all__ = ['pathlib']

from collections.abc import Any, Callable
import pathlib
from ._builtins import UNSET

class LimDepth:
    def __init__(self, min_depth: int = 0, max_depth: None | int = None):
        self.min = min_depth
        self.max = max_depth

    @property
    def min(self):
        return self._min
    @min.setter
    def min(self, v: int):
        if not isinstance(v, int):
            raise TypeError("Can only set integer values.")
        if v < 0:
            raise ValueError("Limit values must be greater than or equal to zero.")
        if v > self.max:
            raise ValueError("Limit values must be greater than or equal to zero.")
        
    
    @property
    def max(self):
        return self._max

    def __iadd__(self, n: int) -> None:
        if not isinstance(n, int):
            raise TypeError("Can only add integer values.")
        self.min += n
        self.max += n
    
    def __isub__(self, n: int) -> None:
        if not isinstance(n, int):
            raise TypeError("Can only substract integer values.")
        self.min -= n
        self.max -= n


def _nullfilter(_: pathlib.Path):
    return True



def _ls(self: pathlib.Path,
        recursive: bool = False,
        follow_symlinks: bool | pathlib.Path = False,
        sort_directories_first: bool = True,
        min_depth: int = 0,
        max_depth: None | int = None,
        filter: None | Callable[[pathlib.Path], bool] = None)
       -> list[pathlib.Path, ...]:
    # TODO: Maybe add options below
    # formatter: None | Callable[[pathlib.Path], Any] = None
    # sort_key: None | Callable[[pathlib.Path, Any], list[list[Any, ...], pathlib.Path]] = None
    if min_depth or max_depth:
        recursive = True
    
