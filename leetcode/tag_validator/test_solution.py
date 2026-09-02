import pytest

from leetcode_py import logged_test

from .helpers import assert_is_valid, run_is_valid
from .solution import Solution


class TestTagValidator:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "code, expected",
        [
            ("<DIV>This is the first line <![CDATA[<div>]]></DIV>", True),
            ("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>", True),
            ("<A>  <B> </A>   </B>", False),
            ("<A></A>", True),
            ("<A></A></A>", False),
            ("a<A></A>", False),
            ("<A>hello</A>b", False),
            ("<div></div>", False),
            ("<A></a>", False),
            ("<A></AB>", False),
            ("<A><![CDATA[<div>]]></A>", True),
            ("<![CDATA[x]]>", False),
            ("<A><B></B></A>", True),
            ("<A><B></A></B>", False),
            ("<ABCDEFGHIJ></ABCDEFGHIJ>", False),
            ("<A></A", False),
            ("<A", False),
            ("<A>content</A>", True),
            ("<A><![CDATA[]]></A>", True),
            ("<AAAAAAAAA></AAAAAAAAA>", True),
            ("<A><A></A>", False),
            ("<A>123</A>", True),
            ("<A></>", False),
            ("<A>x</A><B>y</B>", False),
            ("<A><![CDATA[cdata content]]></A>", True),
            ("<DIV>  divisor is 2  </DIV>", True),
            ("<A><![CDATA[>]]><![CDATA[>]]></A>", True),
            ("<A>1 < 2</A>", False),
            ("<A></A >", False),
            ("<A>  <A>  </A>  </A>", True),
        ],
    )
    def test_is_valid(self, code: str, expected: bool):
        result = run_is_valid(Solution, code)
        assert_is_valid(result, expected)
