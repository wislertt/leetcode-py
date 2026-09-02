class Solution:
    # Time: O(rows + total_sentence_length)
    # Space: O(total_sentence_length) for the joined sentence string
    def words_typing(self, sentence: list[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        n = len(s)
        total = 0
        for _ in range(rows):
            total += cols
            if s[total % n] == " ":
                total += 1
            else:
                while total > 0 and s[(total - 1) % n] != " ":
                    total -= 1
        return total // n
