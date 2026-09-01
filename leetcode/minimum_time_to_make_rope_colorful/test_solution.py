import pytest

from leetcode_py import logged_test

from .helpers import assert_min_cost, run_min_cost
from .solution import Solution


class TestMinimumTimeToMakeRopeColorful:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "colors, needed_time, expected",
        [
            ("abaac", [1, 2, 3, 4, 5], 3),
            ("abc", [1, 2, 3], 0),
            ("aabaa", [1, 2, 3, 4, 1], 2),
            ("a", [7], 0),
            ("aa", [1, 2], 1),
            ("aaa", [1, 2, 3], 3),
            ("aab", [3, 1, 2], 1),
            ("abba", [1, 2, 3, 4], 2),
            ("aabaaa", [1, 3, 2, 4, 5, 6], 10),
            ("zzzaaa", [10, 20, 30, 1, 2, 3], 33),
            ("bcbbbbab", [5725, 899, 4941, 1192, 3913, 8253, 5297, 8540], 10046),
            ("accccab", [3126, 5861, 524, 9519, 5846, 8925, 7380], 12231),
            (
                "bbbbbaaaabb",
                [5101, 6380, 8014, 9748, 8594, 4597, 5083, 2239, 2034, 4117, 9427],
                41076,
            ),
            ("aac", [875, 9488, 6454], 875),
            ("accbcbbcb", [7110, 2488, 736, 9614, 1412, 3757, 7403, 8489, 2136], 4493),
            ("ca", [7237, 1256], 0),
            (
                "cacbaabccccb",
                [9972, 873, 2461, 1761, 4160, 5803, 1694, 2409, 8883, 8661, 4157, 1841],
                19387,
            ),
            ("cbacabcb", [88, 7609, 3924, 4572, 2266, 3165, 2740, 3355], 0),
            ("abbbcaaca", [8288, 3111, 346, 5918, 7824, 8002, 3010, 9337, 1751], 6467),
            ("bcacacc", [3020, 8627, 3259, 1186, 3412, 9791, 4597], 4597),
        ],
    )
    def test_min_cost(self, colors: str, needed_time: list[int], expected: int):
        result = run_min_cost(Solution, colors, needed_time)
        assert_min_cost(result, expected)
