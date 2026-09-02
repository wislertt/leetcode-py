class Solution:
    # Time: O(n)
    # Space: O(1)
    def check_record(self, s: str) -> bool:
        absent = 0
        late_run = 0
        for c in s:
            if c == "A":
                absent += 1
                if absent >= 2:
                    return False
                late_run = 0
            elif c == "L":
                late_run += 1
                if late_run >= 3:
                    return False
            else:
                late_run = 0
        return True
