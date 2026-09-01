class Solution:
    # Time: O(n + q)
    # Space: O(n)
    def vowel_strings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = set("aeiou")
        prefix = [0]
        for word in words:
            is_vowel = word[0] in vowels and word[-1] in vowels
            prefix.append(prefix[-1] + int(is_vowel))
        return [prefix[right + 1] - prefix[left] for left, right in queries]
