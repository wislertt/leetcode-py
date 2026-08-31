import pytest

from leetcode_py import logged_test

from .helpers import assert_autocomplete_system, run_autocomplete_system
from .solution import AutocompleteSystem


class TestDesignSearchAutocompleteSystem:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["AutocompleteSystem", "input", "input", "input", "input"],
                [
                    [["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]],
                    ["i"],
                    [" "],
                    ["a"],
                    ["#"],
                ],
                [
                    None,
                    ["i love you", "island", "i love leetcode"],
                    ["i love you", "i love leetcode"],
                    [],
                    [],
                ],
            ),
            (
                ["AutocompleteSystem", "input", "input", "input", "input", "input", "input"],
                [
                    [["great", "grail", "grotto"], [3, 3, 3]],
                    ["g"],
                    ["r"],
                    ["a"],
                    ["i"],
                    ["l"],
                    ["#"],
                ],
                [
                    None,
                    ["grail", "great", "grotto"],
                    ["grail", "great", "grotto"],
                    ["grail"],
                    ["grail"],
                    ["grail"],
                    [],
                ],
            ),
            (
                [
                    "AutocompleteSystem",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                ],
                [[["hello"], [1]], ["h"], ["e"], ["l"], ["l"], ["o"], ["#"], ["h"]],
                [None, ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], [], ["hello"]],
            ),
            (
                ["AutocompleteSystem", "input", "input"],
                [[["aaa", "aab", "aac"], [1, 1, 1]], ["a"], ["#"]],
                [None, ["aaa", "aab", "aac"], []],
            ),
            (
                ["AutocompleteSystem", "input", "input", "input"],
                [[["x"], [1]], ["y"], ["z"], ["#"]],
                [None, [], [], []],
            ),
            (
                [
                    "AutocompleteSystem",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                ],
                [[["abc"], [2]], ["a"], ["b"], ["#"], ["a"], ["b"], ["c"], ["#"], ["a"]],
                [
                    None,
                    ["abc"],
                    ["abc"],
                    [],
                    ["abc", "ab"],
                    ["abc", "ab"],
                    ["abc"],
                    [],
                    ["abc", "ab"],
                ],
            ),
            (
                ["AutocompleteSystem", "input"],
                [[["solo sentence"], [4]], ["s"]],
                [None, ["solo sentence"]],
            ),
            (
                ["AutocompleteSystem", "input", "input", "input", "input", "input"],
                [[["b bc", "b ab", "b cb"], [1, 2, 3]], ["b"], [" "], ["c"], ["b"], ["#"]],
                [None, ["b cb", "b ab", "b bc"], ["b cb", "b ab", "b bc"], ["b cb"], ["b cb"], []],
            ),
            (
                [
                    "AutocompleteSystem",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                ],
                [
                    [["ir", "iron", "island"], [2, 3, 1]],
                    ["i"],
                    ["r"],
                    ["#"],
                    ["i"],
                    ["s"],
                    ["#"],
                    ["i"],
                    ["r"],
                    ["o"],
                    ["n"],
                ],
                [
                    None,
                    ["iron", "ir", "island"],
                    ["iron", "ir"],
                    [],
                    ["ir", "iron", "island"],
                    ["island"],
                    [],
                    ["ir", "iron", "is"],
                    ["ir", "iron"],
                    ["iron"],
                    ["iron"],
                ],
            ),
            (
                [
                    "AutocompleteSystem",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                ],
                [
                    [["zeta", "zeta beta"], [5, 5]],
                    ["z"],
                    ["e"],
                    ["t"],
                    ["a"],
                    [" "],
                    ["b"],
                    ["e"],
                    ["t"],
                    ["a"],
                ],
                [
                    None,
                    ["zeta", "zeta beta"],
                    ["zeta", "zeta beta"],
                    ["zeta", "zeta beta"],
                    ["zeta", "zeta beta"],
                    ["zeta beta"],
                    ["zeta beta"],
                    ["zeta beta"],
                    ["zeta beta"],
                    ["zeta beta"],
                ],
            ),
            (
                [
                    "AutocompleteSystem",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                    "input",
                ],
                [[["m"], [1]], ["m"], ["#"], ["m"], ["#"], ["m"], ["#"], ["m"]],
                [None, ["m"], [], ["m"], [], ["m"], [], ["m"]],
            ),
            (["AutocompleteSystem", "input"], [[[], []], ["a"]], [None, []]),
        ],
    )
    def test_autocomplete_system(
        self, operations: list[str], inputs: list[list], expected: list[list[str] | None]
    ):
        result, _ = run_autocomplete_system(AutocompleteSystem, operations, inputs)
        assert_autocomplete_system(result, expected)
