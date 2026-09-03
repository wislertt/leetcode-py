class Solution:
    # Time: O(n)
    # Space: O(1)
    def fraction_addition(self, expression: str) -> str:
        num, den = 0, 1
        i, n = 0, len(expression)
        while i < n:
            sign = 1
            if expression[i] in "+-":
                if expression[i] == "-":
                    sign = -1
                i += 1
            numerator = 0
            while i < n and expression[i].isdigit():
                numerator = numerator * 10 + int(expression[i])
                i += 1
            i += 1  # skip '/'
            denominator = 0
            while i < n and expression[i].isdigit():
                denominator = denominator * 10 + int(expression[i])
                i += 1
            num = num * denominator + sign * numerator * den
            den *= denominator
        if num == 0:
            return "0/1"
        a, b = abs(num), den
        while b:
            a, b = b, a % b
        return f"{num // a}/{den // a}"
