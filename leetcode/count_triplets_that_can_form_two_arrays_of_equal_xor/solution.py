class Solution:
    # Time: O(n)
    # Space: O(n)
    def count_triplets(self, arr: list[int]) -> int:
        # a == b means arr[i..k] xors to 0, i.e. pref[i] == pref[k + 1];
        # each such pair (i, k) contributes k - i triplets (one per j in (i, k]).
        total = 0
        count = {0: 1}
        index_sum = {0: 0}
        prefix = 0
        for m, value in enumerate(arr):
            prefix ^= value
            c = count.get(prefix, 0)
            s = index_sum.get(prefix, 0)
            total += c * m - s
            count[prefix] = c + 1
            index_sum[prefix] = s + m + 1
        return total
