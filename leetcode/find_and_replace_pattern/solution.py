class Solution:
    # Time: O(n * m) where n = len(words), m = len(pattern)
    # Space: O(m)
    def find_and_replace_pattern(self, words: list[str], pattern: str) -> list[str]:
        def matches(word: str) -> bool:
            if len(word) != len(pattern):
                return False
            p_to_w: dict[str, str] = {}
            w_to_p: dict[str, str] = {}
            for pc, wc in zip(pattern, word, strict=True):
                if p_to_w.setdefault(pc, wc) != wc or w_to_p.setdefault(wc, pc) != pc:
                    return False
            return True

        return [word for word in words if matches(word)]
