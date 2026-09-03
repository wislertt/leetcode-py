class Solution:
    # Time: O(n + 120^2)
    # Space: O(120)
    def num_friend_requests(self, ages: list[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1
        total = 0
        for x in range(1, 121):
            if count[x] == 0:
                continue
            for y in range(1, 121):
                if count[y] == 0:
                    continue
                if y <= 0.5 * x + 7 or y > x:
                    continue
                total += count[x] * count[y]
                if x == y:
                    total -= count[x]
        return total
