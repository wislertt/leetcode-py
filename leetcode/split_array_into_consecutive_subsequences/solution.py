import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def is_possible(self, nums: list[int]) -> bool:
        chains: list[tuple[int, int]] = []
        for num in nums:
            while chains and chains[0][0] < num - 1:
                if heapq.heappop(chains)[1] < 3:
                    return False
            if chains and chains[0][0] == num - 1:
                _, length = heapq.heappop(chains)
                heapq.heappush(chains, (num, length + 1))
            else:
                heapq.heappush(chains, (num, 1))
        return all(length >= 3 for _, length in chains)
