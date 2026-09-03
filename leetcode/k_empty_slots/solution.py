class Solution:
    # Time: O(n)
    # Space: O(n)
    def k_empty_slots(self, bulbs: list[int], k: int) -> int:
        n = len(bulbs)
        days = [0] * n
        for day, pos in enumerate(bulbs, 1):
            days[pos - 1] = day

        ans = n + 1
        left, right = 0, k + 1
        while right < n:
            valid = True
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + k + 1
                    valid = False
                    break
            if valid:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right + k + 1

        return -1 if ans == n + 1 else ans
