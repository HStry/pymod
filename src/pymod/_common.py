
__all__ = ['UNSET']


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
        return '<UNSET>'

UNSET = UNSET()
