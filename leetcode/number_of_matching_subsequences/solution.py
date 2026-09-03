from collections import defaultdict


class Solution:
    # Time: O(len(s) + total length of all words)
    # Space: O(len(words))

    def num_matching_subseq(self, s: str, words: list[str]) -> int:
        # Bucket words by the next character each one is waiting for.
        waiting: dict[str, list[tuple[int, int]]] = defaultdict(list)
        for idx, word in enumerate(words):
            waiting[word[0]].append((idx, 0))

        matched = 0
        for ch in s:
            for idx, pos in waiting.pop(ch, ()):
                nxt = pos + 1
                if nxt == len(words[idx]):
                    matched += 1
                else:
                    waiting[words[idx][nxt]].append((idx, nxt))
        return matched
