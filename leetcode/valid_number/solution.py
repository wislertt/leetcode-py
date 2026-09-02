class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_number(self, s: str) -> bool:
        i, n = 0, len(s)

        def skip_digits() -> bool:
            nonlocal i
            start = i
            while i < n and s[i].isdigit():
                i += 1
            return i > start

        if s[i] in "+-":
            i += 1
        if skip_digits():
            if i < n and s[i] == ".":
                i += 1
                skip_digits()
        else:
            if i >= n or s[i] != ".":
                return False
            i += 1
            if not skip_digits():
                return False

        if i < n and s[i] in "eE":
            i += 1
            if i < n and s[i] in "+-":
                i += 1
            if not skip_digits():
                return False

        return i == n
