#!/usr/bin/env python3
"""BaseCaching module that defines the parent caching class."""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the cache with an empty dictionary."""
        self.cache_data = {}

    def print_cache(self):
        """Print every key and value of the cache, sorted by key."""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache; it must be implemented by subclasses."""
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """Get an item by key; it must be implemented by subclasses."""
        raise NotImplementedError(
            "get must be implemented in your cache class")
