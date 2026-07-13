class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_turbulence_size(self, arr: list[int]) -> int:
        n = len(arr)
        best = 1
        left = 0
        last_sign = 0  # 1 for prev < next, -1 for prev > next, 0 for equal

        for right in range(1, n):
            if arr[right - 1] < arr[right]:
                sign = 1
            elif arr[right - 1] > arr[right]:
                sign = -1
            else:
                sign = 0

            if sign == 0:
                best = max(best, right - left)
                left = right
                last_sign = 0
            elif sign == last_sign:
                best = max(best, right - left)
                left = right - 1
                last_sign = sign
            else:
                best = max(best, right - left + 1)
                last_sign = sign

        return best
