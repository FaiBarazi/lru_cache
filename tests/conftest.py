import pytest

from simple_lru import LRUCache


@pytest.fixture
def lru_cache():
    _cache = LRUCache(4)
    _cache.put(3, 'C')
    _cache.put(4, 'D')
    _cache.put(1, 'A')
    _cache.put(2, 'B')
    _cache.get(1)
    _cache.get(4)
    return _cache
