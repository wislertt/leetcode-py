class Solution:
    # Time: O(n^m) where n = len(s), m = len(pattern)
    # Space: O(n + m)
    def word_pattern_match(self, pattern: str, s: str) -> bool:
        char_to_word: dict[str, str] = {}
        used: set[str] = set()

        def backtrack(p_idx: int, s_idx: int) -> bool:
            if p_idx == len(pattern) and s_idx == len(s):
                return True
            if p_idx == len(pattern) or s_idx == len(s):
                return False
            char = pattern[p_idx]
            if char in char_to_word:
                word = char_to_word[char]
                if not s.startswith(word, s_idx):
                    return False
                return backtrack(p_idx + 1, s_idx + len(word))
            for end in range(s_idx + 1, len(s) + 1):
                word = s[s_idx:end]
                if word in used:
                    continue
                char_to_word[char] = word
                used.add(word)
                if backtrack(p_idx + 1, end):
                    return True
                del char_to_word[char]
                used.remove(word)
            return False

        return backtrack(0, 0)
