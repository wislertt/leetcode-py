class Solution:
    # Time: O(n * 2^k) where k is the number of letters
    # Space: O(n * 2^k) for the output
    def letter_case_permutation(self, s: str) -> list[str]:
        results: list[str] = [""]

        for ch in s:
            if ch.isalpha():
                results = [prefix + alt for prefix in results for alt in (ch.lower(), ch.upper())]
            else:
                results = [prefix + ch for prefix in results]
        return results
