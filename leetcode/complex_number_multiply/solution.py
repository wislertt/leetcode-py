class Solution:
    # Time: O(len(num1) + len(num2))
    # Space: O(1)
    def complex_number_multiply(self, num1: str, num2: str) -> str:
        a, b = self._parse(num1)
        c, d = self._parse(num2)
        return f"{a * c - b * d}+{a * d + b * c}i"

    def _parse(self, num: str) -> tuple[int, int]:
        real, imag = num[:-1].split("+")
        return int(real), int(imag)
