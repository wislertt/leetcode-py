class Solution:
    # Time: O(n + 26 log 26)
    # Space: O(26)
    def repeat_limited_string(self, s: str, repeat_limit: int) -> str:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1

        parts: list[str] = []
        big = 25
        while big >= 0:
            if counts[big] == 0:
                big -= 1
                continue
            use = min(counts[big], repeat_limit)
            parts.append(chr(ord("a") + big) * use)
            counts[big] -= use
            if counts[big] == 0:
                big -= 1
                continue
            small = big - 1
            while small >= 0 and counts[small] == 0:
                small -= 1
            if small < 0:
                break
            parts.append(chr(ord("a") + small))
            counts[small] -= 1
        return "".join(parts)
