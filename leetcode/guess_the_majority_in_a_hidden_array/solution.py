class ArrayReader:
    # Test-harness API: backs the query/length interface with the hidden array
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def query(self, a: int, b: int, c: int, d: int) -> int:
        total = sum(self.nums[i] for i in (a, b, c, d))
        return 4 if total in (0, 4) else 2 if total in (1, 3) else 0

    def length(self) -> int:
        return len(self.nums)


class Solution:
    # Time: O(n) with n queries, well under the 2 * n budget
    # Space: O(1)
    def guess_majority(self, reader: ArrayReader) -> int:
        # query(0, 1, 2, i) returns the same value as query(0, 1, 2, 3) exactly
        # when nums[i] == nums[3], so indices 4..n-1 split by equality with
        # nums[3]; the count starts at 1 for index 3 itself.
        n = reader.length()
        base = reader.query(0, 1, 2, 3)
        same, diff, k = 1, 0, 0
        for i in range(4, n):
            if reader.query(0, 1, 2, i) == base:
                same += 1
            else:
                diff += 1
                k = i

        # Classify indices 0, 1, 2 against nums[3] using index 4 as the pivot:
        # swapping index 0 into query(1, 2, 4) preserves the result exactly
        # when nums[0] == nums[3], and likewise for indices 1 and 2.
        pivot = reader.query(0, 1, 2, 4)
        for value, idx in (
            (reader.query(1, 2, 3, 4), 0),
            (reader.query(0, 2, 3, 4), 1),
            (reader.query(0, 1, 3, 4), 2),
        ):
            if value == pivot:
                same += 1
            else:
                diff += 1
                k = idx

        if same == diff:
            return -1
        return 3 if same > diff else k
