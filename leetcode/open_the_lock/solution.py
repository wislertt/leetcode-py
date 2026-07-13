from collections import deque


class Solution:
    # Time: O(10^4)
    # Space: O(10^4)
    def open_lock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        queue: deque[tuple[str, int]] = deque([("0000", 0)])
        visited: set[str] = {"0000"}

        while queue:
            state, turns = queue.popleft()
            for i in range(4):
                digit = int(state[i])
                for delta in (1, -1):
                    new_digit = (digit + delta) % 10
                    neighbor = state[:i] + str(new_digit) + state[i + 1 :]
                    if neighbor == target:
                        return turns + 1
                    if neighbor in dead or neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append((neighbor, turns + 1))

        return -1
