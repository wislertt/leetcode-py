import re


class Solution:
    # Time: O(P + B)
    # Space: O(P)
    def most_common_word(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)
        counts: dict[str, int] = {}
        for word in re.findall(r"[a-z]+", paragraph.lower()):
            if word not in banned_set:
                counts[word] = counts.get(word, 0) + 1
        return max(counts, key=lambda w: counts[w])
