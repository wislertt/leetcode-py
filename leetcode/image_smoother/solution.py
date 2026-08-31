class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def image_smoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        result: list[list[int]] = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = count = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        total += img[x][y]
                        count += 1
                result[i][j] = total // count
        return result
