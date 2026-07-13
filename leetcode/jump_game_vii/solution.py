class Solution:
    # Time: O(n)
    # Space: O(n)
    def can_reach(self, s: str, min_jump: int, max_jump: int) -> bool:
        n = len(s)
        if s[n - 1] != "0":
            return False

        reachable = [False] * n
        reachable[0] = True
        window_count = 0

        for i in range(1, n):
            if i >= min_jump and reachable[i - min_jump]:
                window_count += 1
            if i > max_jump and reachable[i - max_jump - 1]:
                window_count -= 1

            if s[i] == "0" and window_count > 0:
                reachable[i] = True

        return reachable[n - 1]
