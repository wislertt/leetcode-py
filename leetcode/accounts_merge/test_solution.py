from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_accounts_merge, run_accounts_merge
from .solution import Solution


class TestAccountsMerge:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "accounts, expected",
        [
            (
                [
                    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                    ["John", "johnsmith@mail.com", "john00@mail.com"],
                    ["Mary", "mary@mail.com"],
                    ["John", "johnnybravo@mail.com"],
                ],
                [
                    ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                    ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                    ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                    ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                    ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
                ],
            )
        ],
    )
    def test_accounts_merge(self, accounts: List[List[str]], expected: List[List[str]]):
        result = run_accounts_merge(Solution, accounts)
        assert_accounts_merge(result, expected)
