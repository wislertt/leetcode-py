import heapq
from collections import Counter


class Solution:
    # Time: O(n log k)
    # Space: O(k)
    def reorganize_string(self, s: str) -> str:
        counts = Counter(s)
        # Impossible when the most frequent char cannot be placed apart.
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""

        # Max-heap by remaining count (negate for Python's min-heap).
        heap: list[tuple[int, str]] = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)

        result: list[str] = []
        while len(heap) >= 2:
            neg_count_a, char_a = heapq.heappop(heap)
            neg_count_b, char_b = heapq.heappop(heap)
            result.append(char_a)
            result.append(char_b)
            if neg_count_a + 1 < 0:
                heapq.heappush(heap, (neg_count_a + 1, char_a))
            if neg_count_b + 1 < 0:
                heapq.heappush(heap, (neg_count_b + 1, char_b))

        if heap:
            result.append(heap[0][1])

        return "".join(result)
