import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_generate_abbreviations,
    assert_generate_abbreviations_count,
    run_generate_abbreviations,
)
from .solution import Solution


class TestGeneralizedAbbreviation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("a", ["1", "a"]),
            ("ab", ["1b", "2", "a1", "ab"]),
            ("abc", ["1b1", "1bc", "2c", "3", "a1c", "a2", "ab1", "abc"]),
            (
                "word",
                [
                    "1o1d",
                    "1o2",
                    "1or1",
                    "1ord",
                    "2r1",
                    "2rd",
                    "3d",
                    "4",
                    "w1r1",
                    "w1rd",
                    "w2d",
                    "w3",
                    "wo1d",
                    "wo2",
                    "wor1",
                    "word",
                ],
            ),
            ("yes", ["1e1", "1es", "2s", "3", "y1s", "y2", "ye1", "yes"]),
            ("aa", ["1a", "2", "a1", "aa"]),
            ("zz", ["1z", "2", "z1", "zz"]),
        ],
    )
    def test_generate_abbreviations(self, word: str, expected: list[str]):
        result = run_generate_abbreviations(Solution, word)
        assert_generate_abbreviations(result, expected)

    @logged_test
    @pytest.mark.parametrize(
        "word, expected_count",
        [
            ("aaaaaa", 64),
            ("aaaaaaaa", 256),
            ("aaaaaaaaaa", 1024),
            ("aaaaaaaaaaaa", 4096),
            ("aaaaaaaaaaaaaaa", 32768),
        ],
    )
    def test_generate_abbreviations_count(self, word: str, expected_count: int):
        result = run_generate_abbreviations(Solution, word)
        assert_generate_abbreviations_count(result, expected_count)
