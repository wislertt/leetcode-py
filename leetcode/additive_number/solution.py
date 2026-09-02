class Solution:
    # Time: O(n^3) - n^2 first-two-number splits, each validated in O(n) steps
    # Space: O(n)
    def is_additive_number(self, num: str) -> bool:
        n = len(num)

        def valid(a_end: int, b_end: int) -> bool:
            first, second = num[:a_end], num[a_end:b_end]
            if len(first) > 1 and first[0] == "0":
                return False
            if len(second) > 1 and second[0] == "0":
                return False
            prev, cur = int(first), int(second)
            end = b_end
            while end < n:
                total = prev + cur
                total_str = str(total)
                if not num.startswith(total_str, end):
                    return False
                end += len(total_str)
                prev, cur = cur, total
            return True

        for a_end in range(1, n - 1):
            for b_end in range(a_end + 1, n):
                if valid(a_end, b_end):
                    return True
        return False
