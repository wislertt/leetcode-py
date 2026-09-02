class Solution:
    # Time: O(n)
    # Space: O(n)
    def sort_transformed_array(self, nums: list[int], a: int, b: int, c: int) -> list[int]:
        n = len(nums)
        result: list[int] = [0] * n

        def f(x: int) -> int:
            return a * x * x + b * x + c

        i, j = 0, n - 1
        idx = n - 1 if a >= 0 else 0
        while i <= j:
            left, right = f(nums[i]), f(nums[j])
            if a >= 0:
                if left >= right:
                    result[idx] = left
                    i += 1
                else:
                    result[idx] = right
                    j -= 1
                idx -= 1
            else:
                if left <= right:
                    result[idx] = left
                    i += 1
                else:
                    result[idx] = right
                    j -= 1
                idx += 1
        return result
