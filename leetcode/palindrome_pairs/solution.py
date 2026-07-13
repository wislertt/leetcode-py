class Solution:
    # Hash map of reversed word -> index. For each word, split into prefix/suffix
    # at every cut. If prefix palindrome, reversed suffix in map -> pair (j, i).
    # If suffix palindrome, reversed prefix in map -> pair (i, j). Handle empty string.
    # Time: O(sum of words[i].length)
    # Space: O(sum of words[i].length)
    def palindrome_pairs(self, words: list[str]) -> list[list[int]]:
        word_to_index = {word: i for i, word in enumerate(words)}
        result: list[list[int]] = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                # Reverse of prefix matches another word and current suffix is palindrome
                # -> that word + word forms palindrome: pair (other, i)
                if prefix == prefix[::-1]:
                    back = suffix[::-1]
                    if back != word and back in word_to_index:
                        result.append([word_to_index[back], i])
                # Reverse of suffix matches another word (not the full word itself) and
                # current prefix is palindrome -> word + that word: pair (i, other)
                if j != len(word) and suffix == suffix[::-1]:
                    front = prefix[::-1]
                    if front != word and front in word_to_index:
                        result.append([i, word_to_index[front]])

        return result
