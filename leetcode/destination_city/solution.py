class Solution:
    # Time: O(E) where E = len(paths)
    # Space: O(E)
    def dest_city(self, paths: list[list[str]]) -> str:
        outgoing = {src for src, _ in paths}
        for _, dst in paths:
            if dst not in outgoing:
                return dst
        return ""
