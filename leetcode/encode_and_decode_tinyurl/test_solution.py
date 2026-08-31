import pytest

from leetcode_py import logged_test

from .helpers import assert_encode_and_decode_tinyurl, run_encode_and_decode_tinyurl
from .solution import Codec


class TestEncodeAndDecodeTinyURL:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["Codec", "encode", "decode"],
                [[], ["https://leetcode.com"], []],
                [None, None, "https://leetcode.com"],
            ),
            (
                ["Codec", "encode", "decode", "encode", "decode"],
                [[], ["a.com"], [], ["b.com"], []],
                [None, None, "a.com", None, "b.com"],
            ),
            (
                ["Codec", "encode", "decode", "encode", "decode"],
                [[], ["x.io"], [], ["x.io"], []],
                [None, None, "x.io", None, "x.io"],
            ),
            (
                ["Codec", "encode", "decode"],
                [[], ["https://a.b/c?d=e#f"], []],
                [None, None, "https://a.b/c?d=e#f"],
            ),
            (
                ["Codec", "encode", "encode", "decode"],
                [[], ["m.io"], ["n.io"], []],
                [None, None, None, "n.io"],
            ),
            (
                ["Codec", "encode", "decode", "encode", "decode", "encode", "decode"],
                [[], ["1.tv"], [], ["2.tv"], [], ["3.tv"], []],
                [None, None, "1.tv", None, "2.tv", None, "3.tv"],
            ),
            (
                ["Codec", "encode", "decode"],
                [[], ["http://tinyurl.com"], []],
                [None, None, "http://tinyurl.com"],
            ),
            (
                ["Codec", "encode", "decode"],
                [[], ["ftp://files.net/doc.pdf"], []],
                [None, None, "ftp://files.net/doc.pdf"],
            ),
            (
                ["Codec", "encode", "decode", "encode", "decode"],
                [
                    [],
                    ["https://leetcode.com/problems/design-tinyurl"],
                    [],
                    ["https://leetcode.com/problems/two-sum"],
                    [],
                ],
                [
                    None,
                    None,
                    "https://leetcode.com/problems/design-tinyurl",
                    None,
                    "https://leetcode.com/problems/two-sum",
                ],
            ),
            (["Codec", "encode", "decode"], [[], ["a"], []], [None, None, "a"]),
            (
                ["Codec", "encode", "encode", "decode"],
                [[], ["same.dev"], ["same.dev"], []],
                [None, None, None, "same.dev"],
            ),
            (
                ["Codec", "encode", "decode", "encode", "decode", "encode", "decode"],
                [[], ["i.org"], [], ["j.org"], [], ["i.org"], []],
                [None, None, "i.org", None, "j.org", None, "i.org"],
            ),
        ],
    )
    def test_encode_and_decode_tinyurl(
        self, operations: list[str], inputs: list[list[str]], expected: list[str | None]
    ):
        result, _ = run_encode_and_decode_tinyurl(Codec, operations, inputs)
        assert_encode_and_decode_tinyurl(result, expected)
