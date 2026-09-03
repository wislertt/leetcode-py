import pytest

from leetcode_py import logged_test

from .helpers import assert_pyramid_transition, run_pyramid_transition
from .solution import Solution


class TestPyramidTransition:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "bottom, allowed, expected",
        [
            ("BCD", ["BCC", "CDE", "CEA", "FFF"], True),
            ("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"], False),
            ("AB", ["ABB"], True),
            ("AB", [], False),
            ("ABC", [], False),
            ("AB", ["AAC"], False),
            ("AA", ["AAA"], True),
            ("AAAA", ["AAB", "ABA", "BAA", "BBB"], True),
            ("ABCDEF", ["ABB", "BCC", "CDD", "DEE", "EFF", "AAB"], True),
            ("ABAB", ["AAB", "BBA", "ABB", "BAA", "AAC", "CCA", "ABC"], True),
            ("AABB", ["AAB", "BBB", "AAC", "BBC", "ACA", "BCA"], False),
            ("ABC", ["AAB", "BBC", "ACA", "AAC"], False),
            ("AAB", ["AAA", "BBB", "AAC", "BBC", "CCA", "CCB"], False),
            ("ABC", ["ABB", "BCA", "ACC", "AAC"], False),
            ("ACB", ["ABB", "ABC", "ACC", "CBA", "CBB"], True),
            ("DAAFB", ["BFC", "CCD", "FDF"], False),
            ("BAB", ["BDA", "CDD"], False),
            ("FC", ["ACE", "BEB", "CBA", "CCF", "DFA", "EBF"], False),
            ("BC", ["ABF", "BCF", "DAC"], True),
            ("DF", ["BCB", "CBF"], False),
            ("ED", ["AEF", "AFB", "CCE", "DBF", "EAD", "EDA", "FCB", "FDF", "FFF"], True),
        ],
    )
    def test_pyramid_transition(self, bottom: str, allowed: list[str], expected: bool):
        result = run_pyramid_transition(Solution, bottom, allowed)
        assert_pyramid_transition(result, expected)
