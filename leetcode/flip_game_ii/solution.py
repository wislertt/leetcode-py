class Solution:
    # Time: O(n^2 * 2^n) where n is the string length, memoized in practice
    # Space: O(2^n)
    def can_win(self, current_state: str) -> bool:
        memo: dict[str, bool] = {}

        def can_win_from(state: str) -> bool:
            if state in memo:
                return memo[state]
            result = False
            for i in range(len(state) - 1):
                if state[i : i + 2] == "++":
                    next_state = state[:i] + "--" + state[i + 2 :]
                    if not can_win_from(next_state):
                        result = True
                        break
            memo[state] = result
            return result

        return can_win_from(current_state)
