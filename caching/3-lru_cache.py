#!/usr/bin/env python3
"""Module that defines LRUCache, a Least Recently Used caching system."""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching system that discards the least recently used item."""

    def __init__(self):
        """Initialize the cache and keep keys ordered by recent use."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Store the item, discarding the least recently used key if full."""
        if key is None or item is None:
            return
        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(lru_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Return the value linked to the key and mark it as recently used."""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
