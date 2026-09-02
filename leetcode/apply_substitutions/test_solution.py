import pytest

from leetcode_py import logged_test

from .helpers import assert_apply_substitutions, run_apply_substitutions
from .solution import Solution


class TestApplySubstitutionsTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "replacements, text, expected",
        [
            ([["A", "abc"], ["B", "def"]], "%A%_%B%", "abc_def"),
            ([["A", "bce"], ["B", "ace"], ["C", "abc%B%"]], "%A%_%B%_%C%", "bce_ace_abcace"),
            ([["A", "hello"]], "%A%", "hello"),
            ([["A", "%B%"], ["B", "xy"]], "%B%_%A%", "xy_xy"),
            ([["A", "a%B%"], ["B", "b"]], "%A%_%B%", "ab_b"),
            ([["A", "%B%B"], ["B", "%C%C"], ["C", "z"]], "%C%_%A%_%B%", "z_zCB_zC"),
            (
                [["A", "%B%%C%"], ["B", "ab"], ["C", "cd"], ["D", "z"]],
                "%A%_%B%_%C%_%D%",
                "abcd_ab_cd_z",
            ),
            (
                [["A", "ab%B%cd"], ["B", "Q"], ["C", "rs"], ["D", "t"]],
                "%B%_%A%_%C%_%D%",
                "Q_abQcd_rs_t",
            ),
            (
                [["A", "%B%"], ["B", "%C%"], ["C", "%D%"], ["D", "ok"]],
                "%A%_%C%_%B%_%D%",
                "ok_ok_ok_ok",
            ),
            (
                [["A", "x"], ["B", "y"], ["C", "%A%z%B%"], ["D", "%C%"]],
                "%D%_%C%_%A%_%B%",
                "xzy_xzy_x_y",
            ),
            ([["A", "aa"], ["B", "bb"], ["C", "cc"]], "%C%_%A%_%B%", "cc_aa_bb"),
            (
                [["A", "%B%a"], ["B", "%C%b"], ["C", "c"], ["D", "d%C%"]],
                "%A%_%B%_%C%_%D%",
                "cba_cb_c_dc",
            ),
            (
                [["A", "z%Q%"], ["Q", "qq"], ["B", "m"], ["Z", "%B%"]],
                "%A%_%Z%_%Q%_%B%",
                "zqq_m_qq_m",
            ),
        ],
    )
    def test_apply_substitutions(self, replacements: list[list[str]], text: str, expected: str):
        result = run_apply_substitutions(Solution, replacements, text)
        assert_apply_substitutions(result, expected)
