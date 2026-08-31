class Solution:
    # Time: O(max(n, log k))
    # Space: O(max(n, log k)) for the output
    def add_to_array_form(self, num: list[int], k: int) -> list[int]:
        result: list[int] = []
        i = len(num) - 1
        carry = k
        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1
            result.append(carry % 10)
            carry //= 10
        return result[::-1]
