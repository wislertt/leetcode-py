class Solution:
    # Time: O(n * L^2) where L is the max word length
    # Space: O(n * L)
    def longest_str_chain(self, words: list[str]) -> int:
        words = sorted(words, key=len)
        chains: dict[str, int] = {}
        best = 0
        for word in words:
            chains[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1 :]
                if predecessor in chains:
                    chains[word] = max(chains[word], chains[predecessor] + 1)
            best = max(best, chains[word])
        return best
