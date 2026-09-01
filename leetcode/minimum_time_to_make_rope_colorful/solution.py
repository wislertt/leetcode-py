class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_cost(self, colors: str, needed_time: list[int]) -> int:
        total = 0
        run_max = needed_time[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                if needed_time[i] < run_max:
                    total += needed_time[i]
                else:
                    total += run_max
                    run_max = needed_time[i]
            else:
                run_max = needed_time[i]
        return total
