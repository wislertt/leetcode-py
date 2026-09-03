class Solution:
    # Time: O(n)
    # Space: O(n) for the output array
    def shortest_to_char(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [n] * n

        prev = -n
        for i, char in enumerate(s):
            if char == c:
                prev = i
            answer[i] = i - prev

        prev = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer
