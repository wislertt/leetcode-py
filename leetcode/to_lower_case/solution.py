class Solution:
    # Time: O(n)
    # Space: O(n)
    def to_lower_case(self, s: str) -> str:
        out: list[str] = []
        for ch in s:
            code = ord(ch)
            out.append(chr(code + 32) if 65 <= code <= 90 else ch)
        return "".join(out)
