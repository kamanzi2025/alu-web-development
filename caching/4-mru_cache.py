#!/usr/bin/env python3
"""Module that defines MRUCache, a Most Recently Used caching system."""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching system that discards the most recently used item."""

    def __init__(self):
        """Initialize the cache and keep keys ordered by recent use."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Store the item, discarding the most recently used key if full."""
        if key is None or item is None:
            return
        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD: {}".format(mru_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Return the value linked to the key and mark it as recently used."""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
