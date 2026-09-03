class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int] | None = None) -> None:
        self.id = id
        self.importance = importance
        self.subordinates = subordinates if subordinates is not None else []


class Solution:
    # Time: O(n)
    # Space: O(n)
    def get_importance(self, employees: list[Employee], id: int) -> int:
        by_id = {employee.id: employee for employee in employees}
        total = 0
        stack = [id]
        while stack:
            employee = by_id[stack.pop()]
            total += employee.importance
            stack.extend(employee.subordinates)
        return total
