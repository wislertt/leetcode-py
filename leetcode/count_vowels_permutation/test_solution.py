import pytest

from leetcode_py import logged_test

from .helpers import assert_count_vowel_permutation, run_count_vowel_permutation
from .solution import Solution


class TestCountVowelsPermutationTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 5),
            (2, 10),
            (3, 19),
            (4, 35),
            (5, 68),
            (6, 129),
            (7, 249),
            (10, 1739),
            (15, 44779),
            (20, 1151090),
            (25, 29599477),
            (50, 227130014),
            (100, 173981881),
            (1000, 89945857),
            (10000, 76428576),
            (20000, 759959057),
        ],
    )
    def test_count_vowel_permutation(self, n: int, expected: int):
        result = run_count_vowel_permutation(Solution, n)
        assert_count_vowel_permutation(result, expected)
