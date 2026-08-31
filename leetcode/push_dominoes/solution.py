class Solution:
    # Time: O(n)
    # Space: O(n)
    def push_dominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n
        f = 0
        for i in range(n):
            if dominoes[i] == "R":
                f = n
            elif dominoes[i] == "L":
                f = 0
            elif f:
                f -= 1
            force[i] += f
        f = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == "L":
                f = n
            elif dominoes[i] == "R":
                f = 0
            elif f:
                f -= 1
            force[i] -= f
        return "".join("." if x == 0 else "R" if x > 0 else "L" for x in force)
