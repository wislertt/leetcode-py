import pytest

from leetcode_py import logged_test

from .helpers import assert_most_visited_pattern, run_most_visited_pattern
from .solution import Solution


class TestAnalyzeUserWebsiteVisitPattern:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "username, timestamp, website, expected",
        [
            (
                ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [
                    "home",
                    "about",
                    "career",
                    "home",
                    "cart",
                    "maps",
                    "home",
                    "home",
                    "about",
                    "career",
                ],
                ["home", "about", "career"],
            ),
            (
                ["ua", "ua", "ua", "ub", "ub", "ub"],
                [1, 2, 3, 4, 5, 6],
                ["a", "b", "a", "a", "b", "c"],
                ["a", "b", "a"],
            ),
            (["u", "u", "u"], [1, 2, 3], ["a", "b", "c"], ["a", "b", "c"]),
            (["u", "u", "u"], [5, 6, 7], ["x", "x", "x"], ["x", "x", "x"]),
            (
                ["u", "u", "u", "v", "v", "v"],
                [1, 2, 3, 4, 5, 6],
                ["b", "a", "c", "b", "a", "c"],
                ["b", "a", "c"],
            ),
            (["u", "u", "u", "u"], [1, 2, 3, 4], ["a", "z", "b", "c"], ["a", "b", "c"]),
            (
                ["u", "u", "u", "u", "u", "v", "v", "v"],
                [1, 2, 3, 4, 5, 6, 7, 8],
                ["a", "b", "a", "b", "c", "a", "b", "c"],
                ["a", "b", "c"],
            ),
            (
                ["u", "u", "u", "solo", "solo"],
                [1, 2, 3, 4, 5],
                ["a", "b", "c", "a", "b"],
                ["a", "b", "c"],
            ),
            (
                ["u", "u", "u", "u", "v", "v", "v", "v"],
                [1, 2, 3, 4, 5, 6, 7, 8],
                ["b", "d", "e", "a", "b", "d", "e", "a"],
                ["b", "d", "a"],
            ),
            (["u", "u", "u", "u"], [1, 2, 3, 4], ["p", "p", "p", "q"], ["p", "p", "p"]),
            (
                ["u", "u", "u", "v", "v", "v", "w", "w", "w"],
                [9, 5, 7, 8, 1, 4, 3, 2, 6],
                ["m", "n", "o", "m", "n", "o", "m", "n", "o"],
                ["n", "o", "m"],
            ),
            (
                ["u", "u", "u", "v", "v", "v"],
                [7, 1, 4, 9, 3, 6],
                ["a", "b", "c", "a", "b", "c"],
                ["b", "c", "a"],
            ),
            (
                ["di", "di", "di", "di", "el", "di", "di", "cy", "di", "al", "cy", "cy"],
                [
                    603020,
                    652710,
                    91595,
                    976829,
                    358271,
                    521397,
                    64021,
                    747030,
                    800611,
                    921008,
                    594994,
                    520757,
                ],
                ["ff", "aa", "dd", "aa", "cc", "bb", "ff", "dd", "bb", "bb", "ff", "ff"],
                ["aa", "bb", "aa"],
            ),
            (
                ["al", "bo", "cy", "cy", "bo", "el", "di", "bo"],
                [544567, 250943, 374132, 253964, 282276, 951921, 908030, 977450],
                ["bb", "aa", "ee", "cc", "aa", "dd", "dd", "ee"],
                ["aa", "aa", "ee"],
            ),
            (
                ["el", "al", "bo", "al", "di", "bo", "bo", "al", "cy", "el", "cy"],
                [
                    823246,
                    469029,
                    120288,
                    299271,
                    569025,
                    891897,
                    265406,
                    638890,
                    598017,
                    716060,
                    175040,
                ],
                ["dd", "ff", "bb", "aa", "aa", "bb", "ee", "bb", "ff", "cc", "bb"],
                ["aa", "ff", "bb"],
            ),
            (
                ["el", "el", "bo", "el", "di", "bo", "di", "el", "bo"],
                [676871, 577558, 787386, 835586, 112060, 527826, 40312, 420365, 917266],
                ["ee", "ff", "bb", "bb", "ff", "ff", "ff", "cc", "dd"],
                ["cc", "ee", "bb"],
            ),
            (
                [
                    "bo",
                    "el",
                    "bo",
                    "al",
                    "bo",
                    "el",
                    "el",
                    "el",
                    "el",
                    "cy",
                    "di",
                    "bo",
                    "el",
                    "al",
                ],
                [
                    632866,
                    154801,
                    191766,
                    314729,
                    452595,
                    855151,
                    3190,
                    156397,
                    615788,
                    473505,
                    356326,
                    763532,
                    271730,
                    417923,
                ],
                [
                    "cc",
                    "aa",
                    "dd",
                    "dd",
                    "ff",
                    "ee",
                    "ee",
                    "dd",
                    "cc",
                    "aa",
                    "aa",
                    "cc",
                    "ee",
                    "ff",
                ],
                ["aa", "cc", "ee"],
            ),
            (
                ["el", "el", "bo", "bo", "cy", "el", "di", "di", "al", "di", "bo", "bo", "bo"],
                [
                    460066,
                    678727,
                    744932,
                    677552,
                    496026,
                    980459,
                    121780,
                    821252,
                    942115,
                    980106,
                    940804,
                    971161,
                    841939,
                ],
                ["dd", "cc", "aa", "ff", "aa", "aa", "dd", "cc", "aa", "dd", "aa", "aa", "ee"],
                ["aa", "aa", "aa"],
            ),
        ],
    )
    def test_most_visited_pattern(
        self, username: list[str], timestamp: list[int], website: list[str], expected: list[str]
    ):
        result = run_most_visited_pattern(Solution, username, timestamp, website)
        assert_most_visited_pattern(result, expected)
