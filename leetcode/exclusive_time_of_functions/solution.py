class Solution:
    # Time: O(L) where L is the number of log entries
    # Space: O(n) for the call stack
    def exclusive_time(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack: list[int] = []
        prev = 0
        for log in logs:
            func_id_s, kind, ts_s = log.split(":")
            func_id, ts = int(func_id_s), int(ts_s)
            if kind == "start":
                if stack:
                    result[stack[-1]] += ts - prev
                stack.append(func_id)
                prev = ts
            else:
                result[stack.pop()] += ts - prev + 1
                prev = ts + 1
        return result
