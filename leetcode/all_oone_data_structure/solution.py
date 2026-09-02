from __future__ import annotations


class Bucket:
    def __init__(self, count: int) -> None:
        self.count = count
        self.keys: set[str] = set()
        self.prev: Bucket = self
        self.next: Bucket = self

    def insert_after(self, node: Bucket) -> None:
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

    def unlink(self) -> None:
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = self.next = self


class AllOne:
    # Doubly linked list of buckets ordered by count, each holding the keys with that
    # count. inc/dec move a key at most one bucket away, so no search is ever needed.
    # Time: O(1) per operation
    # Space: O(n) over the distinct keys stored
    def __init__(self) -> None:
        self.sentinel = Bucket(0)
        self.key_bucket: dict[str, Bucket] = {}

    # Time: O(1)
    # Space: O(1)
    def inc(self, key: str) -> None:
        bucket = self.key_bucket.get(key)
        if bucket is None:
            # New key: it lands at count 1, the bucket closest to the head.
            target = self.sentinel.next
            if target.count != 1:
                target = Bucket(1)
                self.sentinel.insert_after(target)
        else:
            target = bucket.next
            if target.count != bucket.count + 1:
                target = Bucket(bucket.count + 1)
                bucket.insert_after(target)
        self._move(key, bucket, target)

    # Time: O(1)
    # Space: O(1)
    def dec(self, key: str) -> None:
        bucket = self.key_bucket.pop(key)
        target = bucket.prev
        if bucket.count > 1:
            if target.count != bucket.count - 1:
                target = Bucket(bucket.count - 1)
                bucket.prev.insert_after(target)
            self._move(key, bucket, target)
        bucket.keys.discard(key)
        if not bucket.keys:
            bucket.unlink()

    # Time: O(1)
    # Space: O(1)
    def get_max_key(self) -> str:
        return next(iter(self.sentinel.prev.keys), "")

    # Time: O(1)
    # Space: O(1)
    def get_min_key(self) -> str:
        return next(iter(self.sentinel.next.keys), "")

    # Time: O(1)
    # Space: O(1)
    def _move(self, key: str, source: Bucket | None, target: Bucket) -> None:
        if source is not None:
            source.keys.discard(key)
        target.keys.add(key)
        self.key_bucket[key] = target
        if source is not None and not source.keys:
            source.unlink()
