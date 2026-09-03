import pytest

from leetcode_py import logged_test

from .helpers import assert_magic_dictionary, run_magic_dictionary
from .solution import MagicDictionary


class TestImplementMagicDictionary:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["MagicDictionary", "build_dict", "search"], [[], [["a"]], ["b"]], [None, None, True]),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["ab"]], ["cb"]],
                [None, None, True],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["ab"]], ["ac"]],
                [None, None, True],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["ab"]], ["ax"]],
                [None, None, True],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["a"]], ["a"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["ab"]], ["ab"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["ab"]], ["cd"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["ab"]], ["ba"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["ab"]], ["a"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["a"]], ["ab"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["abc"]], ["a"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["a"]], ["abc"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["abc"]], ["ab"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["v"]], ["pxr"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["nxk"]], ["i"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["wl"]], ["pg"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["pm"]], ["l"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["uxj"]], ["x"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["olh"]], ["t"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["so"]], ["mr"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["zz"]], ["vn"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["n"]], ["wg"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["gq"]], ["ta"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["pld"]], ["j"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["byj"]], ["v"]],
                [None, None, False],
            ),
            (
                ["MagicDictionary", "build_dict", "search"],
                [[], [["tc"]], ["v"]],
                [None, None, False],
            ),
        ],
    )
    def test_magic_dictionary(
        self, operations: list[str], inputs: list[list[str]], expected: list[bool | None]
    ):
        result, _ = run_magic_dictionary(MagicDictionary, operations, inputs)
        assert_magic_dictionary(result, expected)
