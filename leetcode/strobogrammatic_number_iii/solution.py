class Solution:
    # Time: O(2^n * n)
    # Space: O(2^n)
    def strobogrammatic_in_range(self, low: str, high: str) -> int:
        def build(length: int, outermost: bool) -> list[str]:
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            results: list[str] = []
            for middle in build(length - 2, False):
                for left, right in ("11", "88", "69", "96"):
                    results.append(left + middle + right)
                if not outermost:
                    results.append("0" + middle + "0")
            return results

        count = 0
        for length in range(len(low), len(high) + 1):
            for candidate in build(length, True):
                if int(low) <= int(candidate) <= int(high):
                    count += 1
        return count
