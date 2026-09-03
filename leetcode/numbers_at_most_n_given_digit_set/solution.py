class Solution:
    # Time: O(log n * len(digits))
    # Space: O(log n)
    def at_most_n_given_digit_set(self, digits: list[str], n: int) -> int:
        ds = sorted(int(d) for d in digits)
        s = str(n)
        k = len(s)
        allowed = set(ds)
        total = sum(len(ds) ** length for length in range(1, k))
        for i, ch in enumerate(s):
            total += sum(d < int(ch) for d in ds) * len(ds) ** (k - 1 - i)
            if int(ch) not in allowed:
                break
        else:
            total += 1
        return total
