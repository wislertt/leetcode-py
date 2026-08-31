class Solution:
    # Time: O(n)
    # Space: O(1)
    def length_of_longest_substring_two_distinct(self, s: str) -> int:
        count: dict[str, int] = {}
        left = 0
        longest = 0
        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            while len(count) > 2:
                left_ch = s[left]
                count[left_ch] -= 1
                if count[left_ch] == 0:
                    del count[left_ch]
                left += 1
            longest = max(longest, right - left + 1)
        return longest
