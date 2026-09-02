class Solution:
    # Time: O(2^m * m) where m = max_choosable_integer
    # Space: O(2^m)
    def can_i_win(self, max_choosable_integer: int, desired_total: int) -> bool:
        if desired_total <= 0:
            return True
        pool = max_choosable_integer * (max_choosable_integer + 1) // 2
        if pool < desired_total:
            return False

        memo: dict[int, bool] = {}

        def dfs(used: int, remaining: int) -> bool:
            if used in memo:
                return memo[used]
            for choice in range(max_choosable_integer):
                bit = 1 << choice
                if used & bit:
                    continue
                if choice + 1 >= remaining or not dfs(used | bit, remaining - choice - 1):
                    memo[used] = True
                    return True
            memo[used] = False
            return False

        return dfs(0, desired_total)
