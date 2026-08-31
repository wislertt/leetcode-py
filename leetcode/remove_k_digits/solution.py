class Solution:
    # Time: O(n)
    # Space: O(n)
    def remove_k_digits(self, num: str, k: int) -> str:
        stack: list[str] = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        if k:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"
