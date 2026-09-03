from collections import Counter


def match_count(a: str, b: str) -> int:
    return sum(x == y for x, y in zip(a, b, strict=True))


class Master:
    # Test-harness API: backs the guess interface with the hidden secret word
    def __init__(self, secret: str, words: list[str], allowed_guesses: int) -> None:
        self.secret = secret
        self.wordset = set(words)
        self.allowed_guesses = allowed_guesses
        self.calls = 0
        self.found = False

    def guess(self, word: str) -> int:
        self.calls += 1
        if word not in self.wordset:
            return -1
        matches = sum(a == b for a, b in zip(word, self.secret, strict=True))
        if matches == len(self.secret):
            self.found = True
        return matches

    def outcome(self) -> bool:
        return self.found and self.calls <= self.allowed_guesses


class Solution:
    # Time: O(g * n^2) for n candidates over g guesses
    # Space: O(n)
    def find_secret_word(self, words: list[str], master: Master) -> None:
        candidates = list(words)
        while len(candidates) > 1:
            guess = min(candidates, key=lambda w: self._worst_bucket(w, candidates))
            matches = master.guess(guess)
            candidates = [w for w in candidates if match_count(w, guess) == matches]
        if candidates:
            master.guess(candidates[0])

    def _worst_bucket(self, word: str, candidates: list[str]) -> int:
        counts = Counter(match_count(c, word) for c in candidates)
        return max(counts.values())
