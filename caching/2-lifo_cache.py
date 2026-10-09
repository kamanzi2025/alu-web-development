#!/usr/bin/env python3
"""Module that defines LIFOCache, a Last-In First-Out caching system."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system that discards the last put item when full."""

    def __init__(self):
        """Initialize the cache and the tracker of the last key put."""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Store the item, discarding the last put key if the cache is full."""
        if key is None or item is None:
            return
        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print("DISCARD: {}".format(self.last_key))
        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Return the value linked to the key, or None if it is missing."""
        if key is None:
            return None
        return self.cache_data.get(key)
