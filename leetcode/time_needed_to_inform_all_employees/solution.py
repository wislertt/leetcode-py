class Solution:
    # Time: O(n)
    # Space: O(n)
    def num_of_minutes(
        self, n: int, head_id: int, manager: list[int], inform_time: list[int]
    ) -> int:
        children: list[list[int]] = [[] for _ in range(n)]
        for employee, boss in enumerate(manager):
            if boss != -1:
                children[boss].append(employee)

        total = 0
        stack = [(head_id, inform_time[head_id])]
        while stack:
            employee, elapsed = stack.pop()
            total = max(total, elapsed)
            for child in children[employee]:
                stack.append((child, elapsed + inform_time[child]))
        return total
