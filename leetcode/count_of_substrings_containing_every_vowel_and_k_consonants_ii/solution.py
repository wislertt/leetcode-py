class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_of_substrings(self, word: str, k: int) -> int:
        def at_least(min_k: int) -> int:
            vowel_counts: dict[str, int] = {}
            consonants = 0
            total = 0
            left = 0
            for right, ch in enumerate(word):
                if ch in "aeiou":
                    vowel_counts[ch] = vowel_counts.get(ch, 0) + 1
                else:
                    consonants += 1
                while len(vowel_counts) == 5 and consonants >= min_k:
                    total += len(word) - right
                    left_ch = word[left]
                    if left_ch in "aeiou":
                        vowel_counts[left_ch] -= 1
                        if vowel_counts[left_ch] == 0:
                            del vowel_counts[left_ch]
                    else:
                        consonants -= 1
                    left += 1
            return total

        return at_least(k) - at_least(k + 1)
