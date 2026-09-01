import pytest

from leetcode_py import logged_test

from .helpers import assert_min_operations, run_min_operations
from .solution import Solution


class TestCrawlerLogFolder:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "logs, expected",
        [
            (["d1/", "d2/", "../", "d21/", "./"], 2),
            (["d1/", "d2/", "./", "d3/", "../", "d31/"], 3),
            (["d1/", "../", "../", "../"], 0),
            (["./"], 0),
            (["../"], 0),
            (["a/"], 1),
            (["a/", "b/", "c/"], 3),
            (["a/", "b/", "../", "../"], 0),
            (["a/", "../", "b/", "../", "c/", "c1/"], 2),
            (["d1/", "d2/", "d3/", "../", "d4/"], 3),
            (["./", "./", "./"], 0),
            (["x1/", "./", "../", "y2/", "./", "../"], 0),
            (["a1b2/"], 1),
            (["a/", "b/", "c/", "d/", "e/", "../", "../", "../", "../"], 1),
            (["a1/", "a2/", "a3/", "a4/", "a5/", "a6/", "a7/", "a8/", "a9/", "a10/"], 10),
            (["deep1/", "deep2/", "../", "../", "../"], 0),
            (["p/", "./", "q/", "../", "./", "r/"], 2),
            (["l1/", "l2/", "l3/", "../", "l4/", "l5/", "../", "../", "../"], 1),
        ],
    )
    def test_min_operations(self, logs: list[str], expected: int):
        result = run_min_operations(Solution, logs)
        assert_min_operations(result, expected)
