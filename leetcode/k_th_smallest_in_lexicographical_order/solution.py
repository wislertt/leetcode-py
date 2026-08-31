class Solution:
    # Time: O(log(n)^2)
    # Space: O(1)
    def find_kth_number(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k:
            steps = self._count_steps(n, curr)
            if steps <= k:
                # skip the whole subtree rooted at curr
                curr += 1
                k -= steps
            else:
                # descend into the subtree
                curr *= 10
                k -= 1
        return curr

    def _count_steps(self, n: int, prefix: int) -> int:
        # count numbers in [1, n] starting with `prefix`
        steps = 0
        first = prefix
        last = prefix
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps
