class Solution:
    # Time: O(n)
    # Space: O(n)
    def sum_subarray_mins(self, arr: list[int]) -> int:
        mod = 1_000_000_007
        n = len(arr)
        stack: list[int] = []
        prev = [0] * n
        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        next_ = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_[i] = stack[-1] if stack else n
            stack.append(i)
        return sum(value * (i - prev[i]) * (next_[i] - i) for i, value in enumerate(arr)) % mod
