import pytest

from leetcode_py import logged_test

from .helpers import assert_partition_labels, run_partition_labels
from .solution import Solution


class TestPartitionLabels:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("ababcbacadefegdehijhklij", [9, 7, 8]),
            ("eccbbbbdec", [10]),
            ("a", [1]),
            ("ab", [1, 1]),
            ("aaa", [3]),
            ("abc", [1, 1, 1]),
            ("abac", [3, 1]),
            ("aab", [2, 1]),
            ("ababcc", [4, 2]),
            ("xxyxx", [5]),
            ("abba", [4]),
            ("z", [1]),
            ("aabbcc", [2, 2, 2]),
        ],
    )
    def test_partition_labels(self, s: str, expected: list[int]):
        result = run_partition_labels(Solution, s)
        assert_partition_labels(result, expected)
