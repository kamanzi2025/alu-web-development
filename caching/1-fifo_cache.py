#!/usr/bin/env python3
"""Module that defines FIFOCache, a First-In First-Out caching system."""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that discards the first inserted item when full."""

    def __init__(self):
        """Initialize the cache and keep keys in their insertion order."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Store the item, discarding the oldest key if the cache is full."""
        if key is None or item is None:
            return
        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(first_key))
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key, or None if it is missing."""
        if key is None:
            return None
        return self.cache_data.get(key)
