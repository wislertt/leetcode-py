import pytest

from leetcode_py import logged_test

from .helpers import assert_partition_string, run_partition_string
from .solution import Solution


class TestOptimalPartitionOfString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abacaba", 4),
            ("ssssss", 6),
            ("a", 1),
            ("ab", 1),
            ("ba", 1),
            ("aa", 2),
            ("abcabcabc", 3),
            ("abacdec", 3),
            ("hklp", 1),
            ("ssssssssssssssssssss", 20),
            ("abcdefghijklmnopqrstuvwxyz", 1),
            ("zyxwvutsrqponmlkjihgfedcba", 1),
            ("abba", 2),
            ("banana", 3),
            ("eecodequestion", 4),
            ("partitionstring", 3),
        ],
    )
    def test_partition_string(self, s: str, expected: int):
        result = run_partition_string(Solution, s)
        assert_partition_string(result, expected)
