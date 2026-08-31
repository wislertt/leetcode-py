class Solution:
    # Time: O(1)  # num < 2^31 bounds the word count
    # Space: O(1)
    BELOW_20: tuple[str, ...] = (
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    )
    TENS: tuple[str, ...] = (
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    )
    THOUSANDS: tuple[str, ...] = ("", "Thousand", "Million", "Billion")

    def _three_digit(self, num: int) -> list[str]:
        """Convert 0 <= num < 1000 to words, e.g. 123 -> ['One', 'Hundred', ...]."""
        if num == 0:
            return []
        if num < 20:
            return [self.BELOW_20[num]]
        if num < 100:
            words = [self.TENS[num // 10]]
            if num % 10:
                words.append(self.BELOW_20[num % 10])
            return words
        words = [self.BELOW_20[num // 100], "Hundred"]
        words.extend(self._three_digit(num % 100))
        return words

    def number_to_words(self, num: int) -> str:
        if num == 0:
            return "Zero"
        words: list[str] = []
        for unit in range(3, -1, -1):
            chunk = num // 1000**unit
            if chunk:
                words.extend(self._three_digit(chunk))
                if unit:
                    words.append(self.THOUSANDS[unit])
                num %= 1000**unit
        return " ".join(words)
