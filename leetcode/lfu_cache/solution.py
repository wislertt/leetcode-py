from collections import OrderedDict, defaultdict


class LFUCache:
    # Time: O(1) amortized per get/put
    # Space: O(capacity)
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val: dict[int, int] = {}
        self.key_to_freq: dict[int, int] = {}
        self.freq_to_keys: dict[int, OrderedDict[int, None]] = defaultdict(OrderedDict)

    def _touch(self, key: int) -> None:
        """Increment frequency of key and move it to the next frequency bucket."""
        freq = self.key_to_freq[key]
        bucket = self.freq_to_keys[freq]
        bucket.pop(key)
        if not bucket:
            if self.min_freq == freq:
                self.min_freq += 1
            del self.freq_to_keys[freq]
        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_to_keys[new_freq][key] = None

    # Time: O(1)
    # Space: O(1)
    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._touch(key)
        return self.key_to_val[key]

    # Time: O(1)
    # Space: O(1)
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._touch(key)
            return
        if len(self.key_to_val) >= self.capacity:
            # Evict least frequently used; ties broken by least recently used.
            min_bucket = self.freq_to_keys[self.min_freq]
            evict_key, _ = min_bucket.popitem(last=False)
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]
            if not min_bucket:
                del self.freq_to_keys[self.min_freq]
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
