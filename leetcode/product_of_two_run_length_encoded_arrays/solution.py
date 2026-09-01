class Solution:
    # Time: O(m + n)
    # Space: O(1) extra (excluding the output)
    def find_rle_array(
        self, encoded1: list[list[int]], encoded2: list[list[int]]
    ) -> list[list[int]]:
        result: list[list[int]] = []
        i = j = 0
        left1 = encoded1[0][1]
        left2 = encoded2[0][1]
        while i < len(encoded1) and j < len(encoded2):
            take = min(left1, left2)
            product = encoded1[i][0] * encoded2[j][0]
            if result and result[-1][0] == product:
                result[-1][1] += take
            else:
                result.append([product, take])
            left1 -= take
            left2 -= take
            if left1 == 0:
                i += 1
                if i < len(encoded1):
                    left1 = encoded1[i][1]
            if left2 == 0:
                j += 1
                if j < len(encoded2):
                    left2 = encoded2[j][1]
        return result
