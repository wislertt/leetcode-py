from functools import cache


class Solution:
    # Time: O(n^4) worst case, Space: O(n^3)
    def remove_boxes(self, boxes: list[int]) -> int:
        @cache
        def dp(left: int, right: int, k: int) -> int:
            if left > right:
                return 0
            # Grow the leftmost run so boxes[left..end] share one color.
            end = left
            while end + 1 <= right and boxes[end + 1] == boxes[end]:
                end += 1
            attached = k + (end - left + 1)
            best = attached * attached + dp(end + 1, right, 0)
            for mid in range(end + 1, right + 1):
                if boxes[mid] == boxes[left] and boxes[mid - 1] != boxes[mid]:
                    best = max(
                        best,
                        dp(end + 1, mid - 1, 0) + dp(mid, right, attached),
                    )
            return best

        return dp(0, len(boxes) - 1, 0)
