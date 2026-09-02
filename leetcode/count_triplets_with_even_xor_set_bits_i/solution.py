class Solution:
    # Time: O(len(a) + len(b) + len(c))
    # Space: O(1)
    def triplet_count(self, a: list[int], b: list[int], c: list[int]) -> int:
        cnt1 = [0, 0]
        cnt2 = [0, 0]
        cnt3 = [0, 0]
        for x in a:
            cnt1[x.bit_count() & 1] += 1
        for x in b:
            cnt2[x.bit_count() & 1] += 1
        for x in c:
            cnt3[x.bit_count() & 1] += 1
        ans = 0
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if (i + j + k) % 2 == 0:
                        ans += cnt1[i] * cnt2[j] * cnt3[k]
        return ans
