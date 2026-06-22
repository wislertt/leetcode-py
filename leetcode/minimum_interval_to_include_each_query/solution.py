import heapq


class Solution:
    # Time: O((n + q) log n) - n intervals, q queries
    # Space: O(n)
    def min_interval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        sorted_queries = sorted(range(len(queries)), key=lambda i: queries[i])

        result = [-1] * len(queries)
        min_heap: list[tuple[int, int]] = []  # (size, right)
        interval_idx = 0

        for query_idx in sorted_queries:
            query_val = queries[query_idx]

            # Add all intervals that start at or before this query value.
            while interval_idx < len(intervals) and intervals[interval_idx][0] <= query_val:
                left, right = intervals[interval_idx]
                heapq.heappush(min_heap, (right - left + 1, right))
                interval_idx += 1

            # Remove intervals that ended before this query value.
            while min_heap and min_heap[0][1] < query_val:
                heapq.heappop(min_heap)

            if min_heap:
                result[query_idx] = min_heap[0][0]

        return result
