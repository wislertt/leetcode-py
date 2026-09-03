class Solution:
    # Time: O(10^2 * n) piece starts are bounded by 10 digits each
    # Space: O(n) for the sequence and recursion
    def split_into_fibonacci(self, num: str) -> list[int]:
        limit = 2**31
        n = len(num)

        for i in range(1, min(n, 10) + 1):
            if num[0] == "0" and i > 1:
                break
            first = int(num[:i])
            if first >= limit:
                break
            for j in range(1, min(n - i, 10) + 1):
                if num[i] == "0" and j > 1:
                    break
                second = int(num[i : i + j])
                if second >= limit:
                    break
                seq = [first, second]
                k = i + j
                while k < n:
                    nxt = seq[-1] + seq[-2]
                    if nxt >= limit or not num.startswith(str(nxt), k):
                        break
                    seq.append(nxt)
                    k += len(str(nxt))
                if k == n and len(seq) >= 3:
                    return seq
        return []
