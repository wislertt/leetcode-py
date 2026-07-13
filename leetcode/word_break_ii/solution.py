class Solution:
    # Time: O(2^n * n) worst case (all segmentations), bounded by answer size
    # Space: O(n * 2^n) for memo storage
    def word_break(self, s: str, word_dict: list[str]) -> list[str]:
        words = set(word_dict)

        # Memo: index -> list of sentences covering s[index:]
        memo: dict[int, list[str]] = {}

        def backtrack(start: int) -> list[str]:
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            sentences: list[str] = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    for sub_sentence in backtrack(end):
                        if sub_sentence:
                            sentences.append(word + " " + sub_sentence)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return backtrack(0)
