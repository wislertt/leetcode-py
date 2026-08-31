class Solution:
    # Time: O(2^n)
    # Space: O(2^n)
    def find_strobogrammatic(self, n: int) -> list[str]:
        def build(length: int) -> list[str]:
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            results: list[str] = []
            for middle in build(length - 2):
                for left, right in ("11", "88", "69", "96"):
                    results.append(left + middle + right)
                if length != n:
                    results.append("0" + middle + "0")
            return results

        return build(n)
