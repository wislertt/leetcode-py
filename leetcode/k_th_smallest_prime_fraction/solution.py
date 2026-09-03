from fractions import Fraction


class Solution:
    # Time: O(n * log(1/gap)) where gap is the smallest difference between two
    # distinct fractions (>= 1 / (3 * 10^4)^2), so ~31 counting passes.
    # Space: O(1)
    def kth_smallest_prime_fraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        lo, hi = Fraction(0), Fraction(1)
        # Smallest gap between two distinct fractions a/b and c/d (values <= 3 * 10^4)
        # is >= 1 / (3 * 10^4)^2, so once the bracket is narrower the answer fraction
        # is isolated and the best fraction below `hi` is exactly the k-th smallest.
        limit = Fraction(1, 9 * 10**8)
        best = [arr[0], arr[-1]]
        while hi - lo >= limit:
            mid = (lo + hi) / 2
            count = 0
            i = 0
            num, den = 0, 1
            for j in range(1, n):
                while arr[i] * mid.denominator < arr[j] * mid.numerator:
                    i += 1
                count += i
                if i > 0 and num * arr[j] < arr[i - 1] * den:
                    num, den = arr[i - 1], arr[j]
            if count < k:
                lo = mid
            else:
                hi = mid
                best = [num, den]
        return best
