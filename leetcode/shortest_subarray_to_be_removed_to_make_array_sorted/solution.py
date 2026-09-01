class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_length_of_shortest_subarray(self, arr: list[int]) -> int:
        n = len(arr)
        end = n - 1
        while end > 0 and arr[end - 1] <= arr[end]:
            end -= 1
        result = end
        start = 0
        while start < end and (start == 0 or arr[start - 1] <= arr[start]):
            while end < n and arr[end] < arr[start]:
                end += 1
            result = min(result, end - start - 1)
            start += 1
        return result
