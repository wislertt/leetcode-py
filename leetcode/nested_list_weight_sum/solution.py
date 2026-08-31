from typing import Any


class Solution:
    # Time: O(n) — every integer visited once (n = total elements)
    # Space: O(d) — recursion depth equals nesting depth
    def depth_sum(self, nested_list: list[Any]) -> int:
        def dfs(items: list[Any], depth: int) -> int:
            return sum(
                item * depth if isinstance(item, int) else dfs(item, depth + 1) for item in items
            )

        return dfs(nested_list, 1)
