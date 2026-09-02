import pytest

from leetcode_py import logged_test

from .helpers import assert_max_length, run_max_length
from .solution import Solution


class TestCuttingRibbons:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ribbons, k, expected",
        [
            ([9, 7, 5], 3, 5),
            ([7, 5, 9], 4, 4),
            ([5, 7, 9], 22, 0),
            ([1], 1, 1),
            ([5], 5, 1),
            ([10], 3, 3),
            ([100], 1, 100),
            ([1, 1, 1, 1], 4, 1),
            ([2, 2, 2], 3, 2),
            ([4, 4, 4], 7, 1),
            ([100000], 1, 100000),
            ([100000], 100000, 1),
            ([1, 2, 3, 4, 5], 6, 2),
            ([8, 8, 8, 8], 9, 2),
            ([99999, 1], 50000, 1),
            ([3813, 2037, 81424, 19692, 67743, 61913], 79339, 2),
            ([80626, 50252, 14225, 96089, 69717], 51585, 6),
            ([84616], 8622, 9),
            ([9759, 25818, 99543, 16022], 145681, 1),
            ([64073, 15281, 84527, 78889, 67863, 23560], 290062, 1),
            ([89494, 58545, 18169, 90077, 69240, 68414], 263003, 1),
            ([38453], 1150, 33),
        ],
    )
    def test_max_length(self, ribbons: list[int], k: int, expected: int):
        result = run_max_length(Solution, ribbons, k)
        assert_max_length(result, expected)
