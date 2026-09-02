class Solution:
    # Time: O(n)
    # Space: O(n)
    def license_key_formatting(self, s: str, k: int) -> str:
        chars = s.replace("-", "").upper()
        first = len(chars) % k or k
        groups = [chars[:first]] if chars else []
        groups.extend(chars[i : i + k] for i in range(first, len(chars), k))
        return "-".join(groups)
