class Solution:
    # Time: O(n * L^2) worst case over group resolution rounds
    # Space: O(n * L)
    def words_abbreviation(self, words: list[str]) -> list[str]:
        n = len(words)
        prefix = [1] * n
        while True:
            groups: dict[str, list[int]] = {}
            for i, word in enumerate(words):
                if prefix[i] > len(word) - 2:
                    continue
                abbrev = word[: prefix[i]] + str(len(word) - prefix[i] - 1) + word[-1]
                groups.setdefault(abbrev, []).append(i)
            conflicts = [group for group in groups.values() if len(group) > 1]
            if not conflicts:
                break
            for group in conflicts:
                for i in group:
                    prefix[i] += 1
        result = []
        for i, word in enumerate(words):
            if prefix[i] > len(word) - 2:
                result.append(word)
            else:
                abbrev = word[: prefix[i]] + str(len(word) - prefix[i] - 1) + word[-1]
                result.append(abbrev if len(abbrev) < len(word) else word)
        return result
