class Solution:
    # Time: O(n)
    # Space: O(1) extra (output excluded)
    def min_operations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answer = [0] * n

        balls = 0
        ops = 0
        for i in range(n):
            answer[i] += ops
            if boxes[i] == "1":
                balls += 1
            ops += balls

        balls = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            answer[i] += ops
            if boxes[i] == "1":
                balls += 1
            ops += balls

        return answer
