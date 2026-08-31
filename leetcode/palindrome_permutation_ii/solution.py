from collections import Counter


class Solution:
    # Time: O(n * (n/2)!) for generating each half permutation
    # Space: O(n)
    def generate_palindromes(self, s: str) -> list[str]:
        counts = Counter(s)
        mid = ""
        for char, count in counts.items():
            if count % 2:
                if mid:
                    return []
                mid = char
                counts[char] -= 1

        results: list[str] = []

        def build(current: str) -> None:
            if all(value == 0 for value in counts.values()):
                results.append(current)
                return
            for char in counts:
                if counts[char] > 0:
                    counts[char] -= 2
                    build(char + current + char)
                    counts[char] += 2

        build(mid)
        return results
