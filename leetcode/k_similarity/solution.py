from collections import deque


class Solution:
    # Time: O(n * n! * n) worst case, pruned heavily by only branching on the
    # first mismatched position and only swapping in a letter that belongs there
    # Space: O(n! * n) for the visited set of intermediate strings
    def k_similarity(self, s1: str, s2: str) -> int:
        queue: deque[str] = deque([s1])
        visited = {s1}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == s2:
                    return steps
                i = 0
                while cur[i] == s2[i]:
                    i += 1
                chars = list(cur)
                for j in range(i + 1, len(chars)):
                    if chars[j] == s2[i] and chars[j] != s2[j]:
                        chars[i], chars[j] = chars[j], chars[i]
                        nxt = "".join(chars)
                        if nxt not in visited:
                            visited.add(nxt)
                            queue.append(nxt)
                        chars[i], chars[j] = chars[j], chars[i]
            steps += 1
        return steps
