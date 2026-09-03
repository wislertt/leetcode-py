class Solution:
    # Time: O((W + Q) * L) where W = len(wordlist), Q = len(queries), L = max word length
    # Space: O(W * L)
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        vowels = set("aeiou")

        def mask(word: str) -> str:
            return "".join("*" if c in vowels else c for c in word.lower())

        words = set(wordlist)
        case_insensitive: dict[str, str] = {}
        vowel_insensitive: dict[str, str] = {}
        for word in wordlist:
            case_insensitive.setdefault(word.lower(), word)
            vowel_insensitive.setdefault(mask(word), word)

        answer: list[str] = []
        for query in queries:
            if query in words:
                answer.append(query)
            elif query.lower() in case_insensitive:
                answer.append(case_insensitive[query.lower()])
            elif mask(query) in vowel_insensitive:
                answer.append(vowel_insensitive[mask(query)])
            else:
                answer.append("")
        return answer
