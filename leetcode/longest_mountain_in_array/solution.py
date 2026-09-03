class Solution:
    # Time: O(n)
    # Space: O(1)
    def longest_mountain(self, arr: list[int]) -> int:
        n = len(arr)
        longest = 0
        i = 1
        while i < n:
            if arr[i - 1] < arr[i]:
                start = i - 1
                while i < n and arr[i - 1] < arr[i]:
                    i += 1
                peak = i - 1
                while i < n and arr[i - 1] > arr[i]:
                    i += 1
                if peak < i - 1:
                    longest = max(longest, i - start)
            else:
                i += 1
        return longest
