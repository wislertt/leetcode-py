from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1) - at most 26 distinct letters
    def num_k_len_substr_no_repeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        cnt = Counter(s[:k])
        ans = int(len(cnt) == k)
        for i in range(k, len(s)):
            cnt[s[i]] += 1
            cnt[s[i - k]] -= 1
            if cnt[s[i - k]] == 0:
                cnt.pop(s[i - k])
            ans += int(len(cnt) == k)
        return ans
