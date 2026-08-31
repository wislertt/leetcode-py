class Solution:
    # Time: O(total characters)
    # Space: O(max_width) excluding the output list
    def full_justify(self, words: list[str], max_width: int) -> list[str]:
        result: list[str] = []
        line: list[str] = []
        line_length = 0

        for word in words:
            # +len(line) accounts for one joining space per existing word
            if line_length + len(line) + len(word) > max_width:
                # Justify the current line: distribute spaces across gaps,
                # assigning extra spaces to the leftmost gaps
                total_spaces = max_width - line_length
                gaps = len(line) - 1
                if gaps == 0:
                    result.append(line[0] + " " * total_spaces)
                else:
                    base, extra = divmod(total_spaces, gaps)
                    row_parts: list[str] = []
                    for i, w in enumerate(line[:-1]):
                        row_parts.append(w)
                        row_parts.append(" " * (base + (1 if i < extra else 0)))
                    row_parts.append(line[-1])
                    result.append("".join(row_parts))
                line = []
                line_length = 0

            line.append(word)
            line_length += len(word)

        # Last line: left-justified with single spaces, padded on the right
        result.append(" ".join(line).ljust(max_width))
        return result
