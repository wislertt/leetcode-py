import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_word_abbr, run_valid_word_abbr
from .solution import ValidWordAbbr


class TestUniqueWordAbbreviation:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["ValidWordAbbr", "is_unique", "is_unique"],
                [["deer", "door", "cake", "card"], ["dear"], ["cart"]],
                [None, False, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["deer", "door", "cake", "card"], ["cane"], ["make"], ["cake"]],
                [None, False, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique"],
                [["deer", "door", "cake", "card"], ["card"], ["door"]],
                [None, True, False],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["deer", "door"], ["dear"], ["door"], ["dore"]],
                [None, False, False, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["it", "is"], ["it"], ["at"], ["is"]],
                [None, True, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["a", "b"], ["a"], ["c"], ["b"]],
                [None, True, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["deer", "deer"], ["deer"], ["dear"], ["deere"]],
                [None, True, False, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["abc", "axc"], ["abc"], ["axc"], ["add"]],
                [None, False, False, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["hello"], ["hello"], ["hellp"], ["hola"]],
                [None, True, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique"],
                [["internationalization"], ["internationalization"], ["inter"]],
                [None, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique"],
                [["internationalization", "internationalizatio"], ["internationalization"]],
                [None, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["aab", "abb"], ["aab"], ["abb"], ["aab"]],
                [None, False, False, False],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["tie", "tie", "tie"], ["tie"], ["tin"], ["tie"]],
                [None, True, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["xyzzyc", "xyzzyc"], ["xyzzyc"], ["yzzzyc"], ["xyzzyc"]],
                [None, True, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["cat", "cow"], ["cat"], ["cow"], ["cut"]],
                [None, True, True, False],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["ddae", "aded", "db"], ["ceac"], ["bde"], ["bdd"]],
                [None, True, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["be", "da", "caabe", "bdaabc"], ["eeed"], ["dca"], ["cabe"]],
                [None, True, True, True],
            ),
            (
                ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"],
                [["cadc", "aaad"], ["dcea"], ["c"], ["adbb"]],
                [None, True, True, True],
            ),
        ],
    )
    def test_is_unique(
        self, operations: list[str], inputs: list[list[str]], expected: list[bool | None]
    ):
        result, _ = run_valid_word_abbr(ValidWordAbbr, operations, inputs)
        assert_valid_word_abbr(result, expected)
