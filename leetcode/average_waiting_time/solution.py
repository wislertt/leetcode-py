class Solution:
    # Time: O(n)
    # Space: O(1)
    def average_waiting_time(self, customers: list[list[int]]) -> float:
        now = 0
        total_wait = 0
        for arrival, time in customers:
            now = max(now, arrival) + time
            total_wait += now - arrival
        return total_wait / len(customers)
