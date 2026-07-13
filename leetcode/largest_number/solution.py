from functools import cmp_to_key


class Solution:
    # Time: O(k * n log n) — comparator does string concat of length k
    # Space: O(n * k) for the string keys
    def largest_number(self, nums: list[int]) -> str:
        strs = [str(n) for n in nums]

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        strs.sort(key=cmp_to_key(compare))
        result = "".join(strs)
        # Leading zero means every value was zero
        return "0" if result[0] == "0" else result
