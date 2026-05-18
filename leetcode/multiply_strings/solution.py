class Solution:
    # Time: O(m * n)
    # Space: O(m + n)
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                total = product + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10
        return "".join(str(x) for x in result).lstrip("0")
