LIMIT = 100001


def _smallest_prime_factors() -> list[int]:
    spf = list(range(LIMIT))
    for i in range(2, int(LIMIT**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, LIMIT, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


class Solution:
    # Time: O(n log n + max(nums) log log max(nums))
    # Space: O(max(nums))
    def maximum_score(self, nums: list[int], k: int) -> int:
        mod = 1_000_000_007
        spf = _smallest_prime_factors()

        def prime_score(x: int) -> int:
            count, cur = 0, x
            while cur > 1:
                p = spf[cur]
                count += 1
                while cur % p == 0:
                    cur //= p
            return count

        n = len(nums)
        scores = [prime_score(num) for num in nums]

        left = [-1] * n
        stack: list[int] = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        result = 1
        remaining = k
        candidates = sorted(
            ((nums[i], (i - left[i]) * (right[i] - i)) for i in range(n)), reverse=True
        )
        for value, count in candidates:
            if remaining <= 0:
                break
            use = min(remaining, count)
            result = result * pow(value, use, mod) % mod
            remaining -= use
        return result
