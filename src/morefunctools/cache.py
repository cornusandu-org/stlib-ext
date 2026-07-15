import math
from functools import lru_cache
from functools import wraps
from typing import Optional, Any
from collections.abc import Callable
from moretyping.visualise import VisLink
from .pyexperimental import experimental
from collections import deque

type MaxSize = int | bool

class CacheInfo:
    def __init__(self, *, hits: int, misses: int, maxsize: MaxSize, currsize: int) -> None:
        self.__dict__["locked"] = False
        self.hits = hits
        self.misses = misses
        self.maxsize = maxsize
        self.currsize = currsize

    def lock(self) -> None:
        self.locked = True

    def __setattr__(self, name, value):
        if self.locked == False:
            self.__dict__[name] = value
        else:
            raise RuntimeError("Attempted to modify immutable object: CacheInfo")
        
    def __str__(self) -> str:
        return f"CacheInfo(hits={self.hits}, misses={self.misses}, maxsize={self.maxsize}, currsize={self.currsize})"

@experimental
def fifo_cache(maxsize: MaxSize = True) -> Callable[[Callable], Callable]:
    if isinstance(maxsize, bool):
        maxsize = math.inf if maxsize else 1

    def decorator(function: Callable):
        cache = {}
        cacheList = deque()

        hits, misses = 0, 0

        def cache_clear() -> None:
            cache = {}

        def cache_info() -> CacheInfo:
            info = CacheInfo(hits = hits, misses = misses, maxsize = maxsize, currsize = len(cache.keys()))
            info.lock()
            return info
        
        def cache_entries() -> tuple[*tuple[Any, Any]]:
            return tuple(cache.items())

        @wraps(function)
        def wrapper(*args, **kwargs) -> Any:
            nonlocal hits, misses
            key = VisLink((tuple(args), tuple(kwargs.items()))).string
            if key in cache.keys():
                hits += 1
                return cache.get(key)
            
            misses += 1
            
            value = function(*args, **kwargs)
            cacheList.append(key)
            cache[key] = value

            if len(cacheList) > maxsize:
                removalKey = cacheList.popleft()
                cache.pop(removalKey)

            return value
        
        wrapper.cache_clear = cache_clear
        wrapper.cache_info = cache_info
        wrapper.cache_entries = cache_entries

        return wrapper
    
    return decorator
