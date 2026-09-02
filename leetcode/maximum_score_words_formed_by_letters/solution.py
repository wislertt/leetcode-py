from collections import Counter


class Solution:
    def max_score_words(self, words: list[str], letters: list[str], score: list[int]) -> int:
        word_counts = [Counter(word) for word in words]
        word_scores = [
            sum(score[ord(c) - 97] * cnt for c, cnt in Counter(word).items()) for word in words
        ]
        n = len(words)

        def backtrack(i: int, available: Counter) -> int:
            if i == n:
                return 0
            best = backtrack(i + 1, available)
            counts = word_counts[i]
            if all(available[c] >= cnt for c, cnt in counts.items()):
                for c, cnt in counts.items():
                    available[c] -= cnt
                best = max(best, word_scores[i] + backtrack(i + 1, available))
                for c, cnt in counts.items():
                    available[c] += cnt
            return best

        return backtrack(0, Counter(letters))
