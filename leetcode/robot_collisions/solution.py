class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def survived_robots_healths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        remaining = list(healths)
        stack: list[int] = []
        for i in sorted(range(len(positions)), key=positions.__getitem__):
            if directions[i] == "R":
                stack.append(i)
                continue
            while stack and remaining[i] > 0:
                j = stack[-1]
                if remaining[j] > remaining[i]:
                    remaining[j] -= 1
                    remaining[i] = 0
                elif remaining[j] < remaining[i]:
                    stack.pop()
                    remaining[j] = 0
                    remaining[i] -= 1
                else:
                    stack.pop()
                    remaining[j] = 0
                    remaining[i] = 0
        return [remaining[i] for i in range(len(positions)) if remaining[i] > 0]
