class Solution:
    # Time: O(n * m) where n = len(emails), m = avg email length
    # Space: O(n * m)
    def num_unique_emails(self, emails: list[str]) -> int:
        seen: set[str] = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            seen.add(f"{local}@{domain}")
        return len(seen)
