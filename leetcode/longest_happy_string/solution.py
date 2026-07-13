import heapq


class Solution:
    # Time: O(n log 3) = O(n) where n = a + b + c total chars placed
    # Space: O(n) for the output
    def longest_happy_string(self, a: int, b: int, c: int) -> str:
        # Greedy: always place the most abundant legal char; if it would form a
        # triple, place the second most abundant instead. Maximises length.
        heap: list[tuple[int, str]] = []
        for ch, count in (("a", a), ("b", b), ("c", c)):
            if count > 0:
                heapq.heappush(heap, (-count, ch))

        result: list[str] = []
        while heap:
            neg_count, ch = heapq.heappop(heap)
            # Blocked if the last two placed equal this char (would make a triple).
            if len(result) >= 2 and result[-1] == result[-2] == ch:
                if not heap:
                    break
                neg_count2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                if neg_count2 + 1 < 0:
                    heapq.heappush(heap, (neg_count2 + 1, ch2))
                heapq.heappush(heap, (neg_count, ch))
            else:
                result.append(ch)
                if neg_count + 1 < 0:
                    heapq.heappush(heap, (neg_count + 1, ch))

        return "".join(result)
