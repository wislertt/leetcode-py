from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_mini_parser, run_mini_parser
from .solution import Solution


class TestMiniParser:
    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("324", 324),
            ("[123,[456,[789]]]", [123, [456, [789]]]),
            ("0", 0),
            ("-1", -1),
            ("1000000", 1000000),
            ("-1000000", -1000000),
            ("[]", []),
            ("[[]]", [[]]),
            ("[[],[[]]]", [[], [[]]]),
            ("[1,2,3]", [1, 2, 3]),
            ("[-1,-2,-3]", [-1, -2, -3]),
            ("[1,[2],[3,[4,[5]]]]", [1, [2], [3, [4, [5]]]]),
            ("[[[[5]]]]", [[[[5]]]]),
            ("[[1],2,[3]]", [[1], 2, [3]]),
            ("[-12,[34],[-56]]", [-12, [34], [-56]]),
            ("[1,2,3,4,5,6,7,8,9,10]", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ("[0,[0,[0]]]", [0, [0, [0]]]),
            ("[-1000000,[1000000,-999999]]", [-1000000, [1000000, -999999]]),
            ("[[1,2],[3,4],[5,[6,7]]]", [[1, 2], [3, 4], [5, [6, 7]]]),
        ],
    )
    def test_mini_parser(self, s: str, expected: Any):
        result = run_mini_parser(Solution, s)
        assert_mini_parser(result, expected)
