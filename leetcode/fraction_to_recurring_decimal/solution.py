class Solution:
    # Time: O(denominator) digits emitted, bounded by the answer length
    # Space: O(k) for the remainder-position map, k = cycle length
    def fraction_to_decimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = "-" if (numerator < 0) != (denominator < 0) else ""
        num, den = abs(numerator), abs(denominator)

        whole, remainder = divmod(num, den)
        parts = [str(whole)]

        if remainder:
            seen: dict[int, int] = {}
            digits: list[str] = []
            while remainder and remainder not in seen:
                seen[remainder] = len(digits)
                remainder *= 10
                digits.append(str(remainder // den))
                remainder %= den
            fraction = "".join(digits)
            if remainder:
                cycle_start = seen[remainder]
                fraction = f"{fraction[:cycle_start]}({fraction[cycle_start:]})"
            parts.append(f".{fraction}")

        return sign + "".join(parts)
