from collections import defaultdict


class ValidWordAbbr:
    # Time: __init__ O(n), is_unique O(1) where n is the dictionary size
    # Space: O(n) for the abbreviation-to-words map
    def __init__(self, dictionary: list[str]) -> None:
        self.groups: dict[str, set[str]] = defaultdict(set)
        for word in dictionary:
            self.groups[self.abbr(word)].add(word)

    # Time: O(1)
    # Space: O(1)
    def is_unique(self, word: str) -> bool:
        group = self.groups.get(self.abbr(word))
        return group is None or group == {word}

    # Time: O(1)
    # Space: O(1)
    def abbr(self, word: str) -> str:
        return word if len(word) < 3 else word[0] + str(len(word) - 2) + word[-1]
