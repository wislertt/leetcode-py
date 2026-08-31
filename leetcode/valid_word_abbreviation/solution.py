class Solution:
    # Time: O(n)
    # Space: O(1)
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        m, n = len(word), len(abbr)
        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                count = 0
                while j < n and abbr[j].isdigit():
                    count = count * 10 + int(abbr[j])
                    j += 1
                i += count
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == m and j == n
