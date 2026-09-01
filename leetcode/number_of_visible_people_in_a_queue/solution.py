class Solution:
    # Time: O(n)
    # Space: O(n)
    def can_see_persons_count(self, heights: list[int]) -> list[int]:
        n = len(heights)
        answer = [0] * n
        stack: list[int] = []
        for i in range(n - 1, -1, -1):
            height = heights[i]
            while stack and stack[-1] < height:
                stack.pop()
                answer[i] += 1
            if stack:
                answer[i] += 1
            stack.append(height)
        return answer
