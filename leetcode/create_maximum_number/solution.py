class Solution:
    # Time: O(k * (m + n))
    # Space: O(k)
    def max_number(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def pick(nums: list[int], size: int) -> list[int]:
            drop = len(nums) - size
            stack: list[int] = []
            for digit in nums:
                while drop and stack and stack[-1] < digit:
                    stack.pop()
                    drop -= 1
                stack.append(digit)
            return stack[:size]

        def merge(a: list[int], b: list[int]) -> list[int]:
            merged: list[int] = []
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i:] > b[j:]:
                    merged.append(a[i])
                    i += 1
                else:
                    merged.append(b[j])
                    j += 1
            merged.extend(a[i:])
            merged.extend(b[j:])
            return merged

        best: list[int] = []
        for take1 in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            candidate = merge(pick(nums1, take1), pick(nums2, k - take1))
            if candidate > best:
                best = candidate
        return best
