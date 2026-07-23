import warnings
from functools import wraps
import pytest

def register_test(func):
    func.__test__ = True
    return func

class _TestSuite:
    __targets__ = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__test__ = True

        targets = getattr(cls, "__targets__", tuple())

        if targets is None or len(targets) == 0:
            warnings.warn(f"{cls.__name__} is defined as a test suite, but has no test targets. Please define __targets__", RuntimeWarning)
            cls.__targets__ = tuple()
            targets = tuple()

        for func in targets:
            func.__test__ = True

        for name, func in cls.__dict__.items():
            if type(func) == type and issubclass(func, _TestSuite) and func not in targets:
                warnings.warn(f"{cls.__name__}.{name} appears to be a test suite, but is not registered as one in __targets__", RuntimeWarning)
            elif (not name.startswith("_")) and func not in targets:
                warnings.warn(f"{cls.__name__}.{name} appears to be a test, but is not registered as one in __targets__", RuntimeWarning)

def static_mark_parametrize(*args, **kwargs):
    def decorator(func):
        func = pytest.mark.parametrize(*args, **kwargs)(func)
        return staticmethod(func)
    return decorator

if __name__ == "__main__":
    import os

    os.system("pytest -vv")
