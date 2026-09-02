import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_common_prefix, run_longest_common_prefix
from .solution import Solution


class TestFindTheLengthOfTheLongestCommonPrefix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr1, arr2, expected",
        [
            ([1, 10, 100], [1000], 3),
            ([1, 2, 3], [4, 4, 4], 0),
            ([5655359], [56554], 4),
            ([1223], [43456], 0),
            ([12], [123], 2),
            ([9], [987654], 1),
            ([100000000], [100000000], 9),
            ([1], [1], 1),
            ([12345], [12345678], 5),
            ([98765432], [9876543], 7),
            ([10, 100, 1000], [1, 10, 100], 3),
            ([2, 22, 222], [22, 222, 2222], 3),
            ([17], [28], 0),
            ([12345678], [87654321], 0),
            ([5, 55, 555], [5], 1),
            ([7], [7, 77, 777], 1),
            ([46534, 79353, 73724, 83159], [56058, 49508], 1),
            ([16096, 51061], [8028, 6558, 11348, 61704], 1),
            ([94545, 88789, 34242], [59165, 39082, 37926], 1),
            ([57116, 86326, 58929], [95528], 0),
            ([12462, 86035, 68557, 54977], [96005, 63807, 36912], 1),
            ([14715, 62484, 17673], [78195], 0),
        ],
    )
    def test_longest_common_prefix(self, arr1: list[int], arr2: list[int], expected: int):
        result = run_longest_common_prefix(Solution, arr1, arr2)
        assert_longest_common_prefix(result, expected)
