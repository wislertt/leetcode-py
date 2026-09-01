class Solution:
    # Time: O(n)
    # Space: O(1)
    def best_closing_time(self, customers: str) -> int:
        penalty = customers.count("Y")
        best_penalty = penalty
        best_hour = 0
        for hour, cust in enumerate(customers, start=1):
            if cust == "Y":
                penalty -= 1
            else:
                penalty += 1
            if penalty < best_penalty:
                best_penalty = penalty
                best_hour = hour
        return best_hour
