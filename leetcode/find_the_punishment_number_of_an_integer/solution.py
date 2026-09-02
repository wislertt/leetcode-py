class Solution:
    # Time: O(n * d^2) where d is the digit count of i*i (partition search per i)
    # Space: O(d) recursion depth
    def punishment_number(self, n: int) -> int:
        def can_partition(sq: str, target: int, idx: int = 0, cur: int = 0) -> bool:
            if idx == len(sq):
                return cur == target
            for j in range(idx + 1, len(sq) + 1):
                part = int(sq[idx:j])
                if cur + part > target:
                    break
                if can_partition(sq, target, j, cur + part):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            if can_partition(str(i * i), i):
                total += i * i
        return total
