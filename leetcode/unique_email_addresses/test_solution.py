import pytest

from leetcode_py import logged_test

from .helpers import assert_num_unique_emails, run_num_unique_emails
from .solution import Solution


class TestUniqueEmailAddresses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "emails, expected",
        [
            (
                [
                    "test.email+alex@leetcode.com",
                    "test.e.mail+bob.cathy@leetcode.com",
                    "testemail+david@lee.tcode.com",
                ],
                2,
            ),
            (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"], 3),
            (["a@leetcode.com"], 1),
            (["a.b@c.com", "ab@c.com"], 1),
            (["a+b@c.com", "a@c.com"], 1),
            (["a@b.com", "a@c.com"], 2),
            (["a.b.c@c.com", "abc+c@c.com", "abc@c.com"], 1),
            (["a@b.com", "b@b.com", "a@b.com"], 2),
            ([".+@c.com", "x@y.com"], 2),
            (["a.b+c.d@e.com", "ab@e.com", "a.b@e.com"], 1),
            (["x+y+z@a.com", "x.y@a.com", "xy@a.com", "z@a.com"], 3),
            (["test.email+alex@leetcode.com", "test.email@leet.code.com"], 2),
            (["r@x.com", "r.+@x.com", "r..@x.com"], 1),
            (["ab@e.com", "a.b@e.com", "a.b+c@e.com", "ba@e.com"], 2),
        ],
    )
    def test_num_unique_emails(self, emails: list[str], expected: int):
        result = run_num_unique_emails(Solution, emails)
        assert_num_unique_emails(result, expected)
