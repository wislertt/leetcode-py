MAX_32_BIT = 2**31 - 1


class Solution:
    # Time: O(d) where d is the number of digits in n
    # Space: O(d)
    def next_greater_element(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)

        # Find the rightmost index where digits[i] < digits[i + 1].
        pivot = length - 2
        while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            return -1

        # Smallest digit to the right of pivot that is still larger than it.
        successor = length - 1
        while digits[successor] <= digits[pivot]:
            successor -= 1
        digits[pivot], digits[successor] = digits[successor], digits[pivot]

        # The suffix is non-increasing; reverse it to make it the smallest.
        digits[pivot + 1 :] = reversed(digits[pivot + 1 :])

        result = int("".join(digits))
        return result if result <= MAX_32_BIT else -1
