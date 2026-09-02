class Solution:
    # Time: O(len(s1) * len(s2) + len(s2))
    # Space: O(len(s2))
    def get_max_repetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        m = len(s2)

        # For each possible starting index in s2, scan one block of s1 and
        # record the resulting index plus how many full s2 blocks were matched.
        nxt = [0] * m
        add = [0] * m
        for start in range(m):
            idx = start
            matched = 0
            for ch in s1:
                if ch == s2[idx]:
                    idx += 1
                    if idx == m:
                        idx = 0
                        matched += 1
            nxt[start] = idx
            add[start] = matched

        # Walk block by block; once a start index repeats, the remaining blocks
        # advance in a cycle whose s2-block gain per cycle is constant, so jump
        # over all full cycles at once.
        total = 0
        idx = 0
        seen: dict[int, tuple[int, int]] = {}
        block = 0
        while block < n1:
            if idx in seen:
                prev_block, prev_total = seen[idx]
                cycle_len = block - prev_block
                cycle_gain = total - prev_total
                full_cycles = (n1 - block) // cycle_len
                total += full_cycles * cycle_gain
                block += full_cycles * cycle_len
                if block == n1:
                    break
            seen[idx] = (block, total)
            total += add[idx]
            idx = nxt[idx]
            block += 1

        return total // n2
