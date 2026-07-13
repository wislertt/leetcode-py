from collections import deque


class Solution:
    # Time: O(n) each senator is banned at most once
    # Space: O(n) for the queues
    def predict_party_victory(self, senate: str) -> str:
        n = len(senate)
        radiant: deque[int] = deque(i for i, ch in enumerate(senate) if ch == "R")
        dire: deque[int] = deque(i for i, ch in enumerate(senate) if ch == "D")

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            # Earlier senator bans the other; winner re-enters with a future index.
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"
