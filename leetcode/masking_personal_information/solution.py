class Solution:
    # Time: O(n)
    # Space: O(n)
    def mask_pii(self, s: str) -> str:
        if "@" in s:
            name, domain = s.split("@")
            lower_name = name.lower()
            return f"{lower_name[0]}*****{lower_name[-1]}@{domain.lower()}"
        digits = [c for c in s if c.isdigit()]
        country = len(digits) - 10
        tail = "".join(digits[-4:])
        prefix = "+" + "*" * country if country else ""
        return f"{prefix}-***-***-{tail}" if prefix else f"***-***-{tail}"
