class Solution:
    # Time: O(1)
    # Space: O(1)
    def restore_ip_addresses(self, s: str) -> list[str]:
        results: list[str] = []

        def is_valid_part(part: str) -> bool:
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        def backtrack(start: int, parts: list[str]) -> None:
            if len(parts) == 4:
                if start == len(s):
                    results.append(".".join(parts))
                return
            remaining_digits = len(s) - start
            remaining_parts = 4 - len(parts)
            if remaining_digits < remaining_parts or remaining_digits > remaining_parts * 3:
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                part = s[start : start + length]
                if is_valid_part(part):
                    parts.append(part)
                    backtrack(start + length, parts)
                    parts.pop()

        backtrack(0, [])
        return results
