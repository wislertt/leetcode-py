class Solution:
    # Time: O(n + sum(len(sources[i]) + len(targets[i])))
    # Space: O(n)
    def find_replace_string(
        self, s: str, indices: list[int], sources: list[str], targets: list[str]
    ) -> str:
        match_at: dict[int, int] = {}
        for i, idx in enumerate(indices):
            if s.startswith(sources[i], idx):
                match_at[idx] = i

        pieces: list[str] = []
        i = 0
        while i < len(s):
            j = match_at.get(i)
            if j is None:
                pieces.append(s[i])
                i += 1
            else:
                pieces.append(targets[j])
                i += len(sources[j])
        return "".join(pieces)
