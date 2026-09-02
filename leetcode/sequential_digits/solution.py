class Solution:
    def sequential_digits(self, low: int, high: int) -> list[int]:
        result: list[int] = []
        for length in range(2, 10):
            for start in range(1, 11 - length):
                num = int("".join(str(start + i) for i in range(length)))
                if low <= num <= high:
                    result.append(num)
        return result
