#!/usr/bin/env python3
"""Module that defines BasicCache, a caching system without any limit."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system that stores items without any size limit."""

    def put(self, key, item):
        """Store the item in the cache under the given key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key, or None if it is missing."""
        if key is None:
            return None
        return self.cache_data.get(key)
