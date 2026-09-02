class Solution:
    # Time: O(n!)
    # Space: O(n)
    def construct_distanced_sequence(self, n: int) -> list[int]:
        size = 2 * n - 1
        result = [0] * size
        used = [False] * (n + 1)

        def backtrack(index: int) -> bool:
            if index == size:
                return True
            if result[index] != 0:
                return backtrack(index + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                second = index + num
                if num == 1:
                    result[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used[1] = False
                elif second < size and result[second] == 0:
                    result[index] = result[second] = num
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = result[second] = 0
                    used[num] = False
            return False

        backtrack(0)
        return result
