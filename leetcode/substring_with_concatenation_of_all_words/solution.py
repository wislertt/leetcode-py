from collections import Counter


class Solution:
    # Time: O(word_len * len(s)) - each index enters the window at most once per offset
    # Space: O(len(words)) for the two counters
    def find_substring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_total = len(words)
        concat_len = word_len * word_total
        target = Counter(words)
        result: list[int] = []

        for offset in range(word_len):
            left = offset
            window: Counter[str] = Counter()
            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                window[word] += 1
                while window[word] > target[word]:
                    window[s[left : left + word_len]] -= 1
                    left += word_len
                if right + word_len - left == concat_len:
                    result.append(left)

        return result
