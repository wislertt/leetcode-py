from typing import Any


class Solution:
    # Time: O(n) — every integer visited once (n = total elements)
    # Space: O(d) — recursion depth equals nesting depth
    def depth_sum_inverse(self, nested_list: list[Any]) -> int:
        def dfs(items: list[Any], depth: int) -> tuple[int, int, int]:
            plain = 0
            by_depth = 0
            max_depth = depth
            for item in items:
                if isinstance(item, int):
                    plain += item
                    by_depth += item * depth
                else:
                    p, b, md = dfs(item, depth + 1)
                    plain += p
                    by_depth += b
                    max_depth = max(max_depth, md)
            return plain, by_depth, max_depth

        plain, by_depth, max_depth = dfs(nested_list, 1)
        # sum(v * (max_depth - d + 1)) = (max_depth + 1) * sum(v) - sum(v * d)
        return (max_depth + 1) * plain - by_depth
