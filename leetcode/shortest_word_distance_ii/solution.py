from collections import defaultdict


class WordDistance:
    # Time: O(n) for __init__, O(k + m) per shortest call
    # Space: O(n)
    def __init__(self, words_dict: list[str]) -> None:
        self.indices: defaultdict[str, list[int]] = defaultdict(list)
        for i, word in enumerate(words_dict):
            self.indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        positions1 = self.indices[word1]
        positions2 = self.indices[word2]
        shortest = 10**9
        i = 0
        j = 0
        while i < len(positions1) and j < len(positions2):
            shortest = min(shortest, abs(positions1[i] - positions2[j]))
            if positions1[i] <= positions2[j]:
                i += 1
            else:
                j += 1
        return shortest
