# Caching

This project implements several caching systems in Python 3. Every class
inherits from `BaseCaching` (defined in `base_caching.py`), stores its data in
the `self.cache_data` dictionary, and implements `put(key, item)` and
`get(key)`.

- `put` does nothing if `key` or `item` is `None`.
- `get` returns `None` if `key` is `None` or not in the cache.
- A bounded cache holds at most `BaseCaching.MAX_ITEMS` (4) items. When a
  **new** key is added to a full cache, one key is discarded and
  `DISCARD: <key>` is printed. Updating an existing key never discards.

## Files and cache policies

| File | Class | Policy |
| --- | --- | --- |
| `base_caching.py` | `BaseCaching` | Parent class: defines `MAX_ITEMS`, `cache_data` and `print_cache`. |
| `0-basic_cache.py` | `BasicCache` | No limit; nothing is ever discarded. |
| `1-fifo_cache.py` | `FIFOCache` | **First In, First Out**: discards the key that was inserted first. Updating a key does not change its position. |
| `2-lifo_cache.py` | `LIFOCache` | **Last In, First Out**: discards the key most recently written by `put` (an update counts as the latest put). |
| `3-lru_cache.py` | `LRUCache` | **Least Recently Used**: discards the key that has gone longest without a `put` or successful `get`. |
| `4-mru_cache.py` | `MRUCache` | **Most Recently Used**: discards the key touched most recently by a `put` or successful `get`. |

## Usage

```python
#!/usr/bin/env python3
FIFOCache = __import__('1-fifo_cache').FIFOCache

cache = FIFOCache()
cache.put("A", "Hello")
print(cache.get("A"))
cache.print_cache()
```

## Requirements

- Python 3.7, pycodestyle 2.5
- All files start with `#!/usr/bin/env python3` and are executable
