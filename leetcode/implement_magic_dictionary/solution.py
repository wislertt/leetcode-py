class MagicDictionary:
    # Time: build_dict O(total chars), search O(25 * n)
    # Space: O(total chars)

    def __init__(self) -> None:
        self.words: set[str] = set()

    def build_dict(self, dictionary: list[str]) -> None:
        self.words = set(dictionary)

    def search(self, search_word: str) -> bool:
        for i, kept in enumerate(search_word):
            prefix = search_word[:i]
            suffix = search_word[i + 1 :]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char != kept and prefix + char + suffix in self.words:
                    return True
        return False
