class Solution:
    # Time: O(len(name) + len(typed))
    # Space: O(1)
    def is_long_pressed_name(self, name: str, typed: str) -> bool:
        i = 0
        for j, ch in enumerate(typed):
            if i < len(name) and name[i] == ch:
                i += 1
            elif j == 0 or ch != typed[j - 1]:
                return False
        return i == len(name)
