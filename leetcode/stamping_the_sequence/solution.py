class Solution:
    # Time: O(n^2 * m) worst case, where n = len(target) and m = len(stamp); each
    # stamp erases at least one letter, so there are at most n stamps per pass.
    # Space: O(n) for the working copy of target.
    def moves_to_stamp(self, stamp: str, target: str) -> list[int]:
        chars = list(target)
        stamp_len = len(stamp)
        target_len = len(chars)
        moves: list[int] = []
        done = 0
        # [left, right) is the region still holding letters from target; every
        # useful stamp window must intersect it, otherwise it only writes over '?'.
        left, right = 0, target_len
        while done < target_len:
            placed_at = -1
            low = max(0, left - stamp_len + 1)
            high = min(right, target_len - stamp_len + 1)
            for start in range(low, high):
                covered = 0
                for offset, char in enumerate(stamp):
                    current = chars[start + offset]
                    if current == "?":
                        continue
                    if current != char:
                        break
                    covered += 1
                else:
                    if covered:
                        placed_at = start
                        break
            if placed_at < 0:
                return []
            for offset in range(stamp_len):
                if chars[placed_at + offset] != "?":
                    chars[placed_at + offset] = "?"
                    done += 1
            moves.append(placed_at)
            while left < target_len and chars[left] == "?":
                left += 1
            while right > left and chars[right - 1] == "?":
                right -= 1
        moves.reverse()
        return moves
