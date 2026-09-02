class Solution:
    # Time: O(n)
    # Space: O(n)
    def strong_password_checker(self, password: str) -> int:
        n = len(password)
        missing = 3 - (
            any(c.islower() for c in password)
            + any(c.isupper() for c in password)
            + any(c.isdigit() for c in password)
        )

        runs: list[int] = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            runs.append(j - i)
            i = j

        if n < 6:
            # Insertions cover both the length gap and the missing types.
            return max(6 - n, missing)

        replace = sum(run // 3 for run in runs)
        if n <= 20:
            # A replacement fixes a missing type and breaks a repeat at once.
            return max(missing, replace)

        # Length must shrink to 20; spend deletions where they save a replacement.
        delete = n - 20
        lengths = runs[:]
        remaining = delete
        for mod in (0, 1):
            for idx, run in enumerate(lengths):
                if remaining <= 0:
                    break
                if run >= 3 and run % 3 == mod:
                    spent = min(remaining, mod + 1)
                    lengths[idx] -= spent
                    remaining -= spent
            if remaining <= 0:
                break

        replace_left = sum(run // 3 for run in lengths)
        # Leftover deletions still help: every 3 of them shorten a run past one repeat.
        return delete + max(missing, replace_left - remaining // 3)
