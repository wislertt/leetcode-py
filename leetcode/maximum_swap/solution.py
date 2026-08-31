class Solution:
    # Time: O(d) where d is the number of digits
    # Space: O(d)
    def maximum_swap(self, num: int) -> int:
        digits = list(str(num))
        last: dict[int, int] = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for bigger in range(9, int(d), -1):
                if bigger in last and last[bigger] > i:
                    j = last[bigger]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num
