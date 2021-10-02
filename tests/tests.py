import pytest

from simple_lru import LRUCache


def test_reset():
    lru_cache = LRUCache(4)
    lru_cache.put(3, 'hello')
    lru_cache.reset()
    assert len(lru_cache) == 0


def test_zero_init():
    with pytest.raises(ValueError):
        LRUCache(0)


def test_order(lru_cache):
    # Order should be 3 2 1 4
    keys = list(lru_cache.cache.keys())
    results = [3, 2, 1, 4]
    for i in range(len(keys)):
        assert keys[i] == results[i]


def test_delete(lru_cache):
    lru_cache.delete(3)
    assert len(lru_cache) == 3


def test_max_capacity(lru_cache):
    lru_cache.put(5, 'E')
    assert len(lru_cache) == 4
    assert 3 not in lru_cache.cache.keys()
    least_used = list(lru_cache.cache.keys())[0]
    assert least_used == 2
    last_used = list(lru_cache.cache.keys())[-1]
    assert last_used == 5
