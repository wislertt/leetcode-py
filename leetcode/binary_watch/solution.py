class Solution:
    # Time: O(12 * 60)
    # Space: O(1) excluding the output
    def read_binary_watch(self, turned_on: int) -> list[str]:
        if turned_on > 9:
            return []
        result: list[str] = []
        for hour in range(12):
            for minute in range(60):
                if hour.bit_count() + minute.bit_count() == turned_on:
                    result.append(f"{hour}:{minute:02d}")
        return result
