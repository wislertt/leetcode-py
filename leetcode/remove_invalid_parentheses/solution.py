class Solution:
    # Time: O(2^p) over the p <= 20 parenthesis positions, each kept or removed
    # Space: O(n) recursion depth plus the result set
    def remove_invalid_parentheses(self, s: str) -> list[str]:
        rem_left = rem_right = 0
        for ch in s:
            if ch == "(":
                rem_left += 1
            elif ch == ")":
                if rem_left:
                    rem_left -= 1
                else:
                    rem_right += 1

        results: set[str] = set()
        path: list[str] = []
        n = len(s)

        def dfs(i: int, open_count: int, left_rem: int, right_rem: int) -> None:
            if left_rem + right_rem > n - i:
                return
            if i == n:
                if left_rem == 0 and right_rem == 0 and open_count == 0:
                    results.add("".join(path))
                return
            ch = s[i]
            if ch == "(" and left_rem > 0:
                dfs(i + 1, open_count, left_rem - 1, right_rem)
            elif ch == ")" and right_rem > 0:
                dfs(i + 1, open_count, left_rem, right_rem - 1)
            path.append(ch)
            if ch == "(":
                dfs(i + 1, open_count + 1, left_rem, right_rem)
            elif ch == ")" and open_count > 0:
                dfs(i + 1, open_count - 1, left_rem, right_rem)
            elif ch not in "()":
                dfs(i + 1, open_count, left_rem, right_rem)
            path.pop()

        dfs(0, 0, rem_left, rem_right)
        return list(results)
