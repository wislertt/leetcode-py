import pytest

from leetcode_py import logged_test

from .helpers import assert_can_transform, run_can_transform
from .solution import Solution


class TestSwapAdjacentInLRString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "start, result, expected",
        [
            ("RXXLRXRXL", "XRLXXRRLX", True),
            ("X", "L", False),
            ("L", "L", True),
            ("R", "R", True),
            ("X", "X", True),
            ("XL", "LX", True),
            ("RX", "XR", True),
            ("LX", "XL", False),
            ("XR", "RX", False),
            ("XX", "XX", True),
            ("RL", "RL", True),
            ("XXXX", "XXXX", True),
            ("XLX", "XXL", False),
            ("LXXR", "LXXR", True),
            ("XL", "XL", True),
            ("RXLXL", "XLRLX", False),
            ("XRXR", "RRXX", False),
            ("XXXXRXXXLXX", "XXXXRXXXLXX", True),
            ("RRR", "XRR", False),
            ("LRXXXR", "XRLLXL", False),
            ("LXLX", "XRRX", False),
            ("LXXL", "RXLR", False),
            ("LRXLXX", "LXXXRX", False),
            ("LXRLL", "RRLXX", False),
            ("LRLRX", "LXRXR", False),
            ("LLLL", "XXLL", False),
            ("LXR", "LXR", True),
            ("LXLX", "LLXX", True),
            ("LLL", "LLL", True),
            ("XLXLXXX", "LLXXXXX", True),
            ("LLRLL", "LLRLL", True),
        ],
    )
    def test_can_transform(self, start: str, result: str, expected: bool):
        result = run_can_transform(Solution, start, result)
        assert_can_transform(result, expected)
