import pytest

from leetcode_py import logged_test

from .helpers import assert_is_additive_number, run_is_additive_number
from .solution import Solution


class TestAdditiveNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            ("112358", True),
            ("199100199", True),
            ("1023", False),
            ("000", True),
            ("0000", True),
            ("101", True),
            ("011235", True),
            ("1123581321", True),
            ("1203", False),
            ("211738", True),
            ("112", True),
            ("111", False),
            ("0235", False),
            ("347", True),
            ("13", False),
            ("0", False),
            ("10235", False),
            ("1120", False),
            ("355287139226365591956154725034050", True),
            ("95141933528513722235958194015212461", True),
            ("9974241421184532665111", True),
            ("1016955197129264897782312720", True),
            ("984546", False),
            ("37985807484380683024", False),
        ],
    )
    def test_is_additive_number(self, num: str, expected: bool):
        result = run_is_additive_number(Solution, num)
        assert_is_additive_number(result, expected)
