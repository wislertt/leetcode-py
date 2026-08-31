import pytest

from leetcode_py import logged_test

from .helpers import assert_count_of_atoms, run_count_of_atoms
from .solution import Solution


class TestNumberOfAtoms:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "formula, expected",
        [
            ("H2O", "H2O"),
            ("Mg(OH)2", "H2MgO2"),
            ("K4(ON(SO3)2)2", "K4N2O14S4"),
            ("H", "H"),
            ("H2", "H2"),
            ("Be32", "Be32"),
            ("(H)", "H"),
            ("(H)2", "H2"),
            ("H2Mg", "H2Mg"),
            ("((H)2)3", "H6"),
            ("Mg(H2O)2N", "H4MgNO2"),
            ("Nb2", "Nb2"),
            ("B2O3Si", "B2O3Si"),
            ("Fe16O32", "Fe16O32"),
            ("ZnNe500", "Ne500Zn"),
            ("(((H41)40)41)40", "H2689600"),
        ],
    )
    def test_count_of_atoms(self, formula: str, expected: str):
        result = run_count_of_atoms(Solution, formula)
        assert_count_of_atoms(result, expected)
