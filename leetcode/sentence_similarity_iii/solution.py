class Solution:
    # Time: O(n + m) where n, m are the sentence lengths
    # Space: O(n + m) for the split word lists
    def are_sentences_similar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) < len(words2):
            words1, words2 = words2, words1

        prefix = 0
        while prefix < len(words2) and words1[prefix] == words2[prefix]:
            prefix += 1

        suffix = 0
        while (
            suffix < len(words2) - prefix
            and words1[len(words1) - 1 - suffix] == words2[len(words2) - 1 - suffix]
        ):
            suffix += 1

        return prefix + suffix == len(words2)
