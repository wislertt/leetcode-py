import pytest

from leetcode_py import logged_test

from .helpers import assert_is_symmetric, run_is_symmetric
from .solution import Solution


class TestSymmetricTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 2, 3, 4, 4, 3], True),
            ([1, 2, 2, None, 3, None, 3], False),
            ([1], True),
            ([1, 2, 2], True),
            ([1, 2, 3], False),
            ([1, None, 2], False),
            ([1, 2, None], False),
            ([1, 2, 2, 3, None, None, 3], True),
            ([1, 2, 2, 3], False),
            ([1, 2, 2, 3, 4, 4, 5], False),
            ([1, 2, 2, 3, 5, 4, 3], False),
            ([1, 2, 2, None, 3, None, 4], False),
            ([5, 1, 1, 2, None, None, 2], True),
            ([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5], True),
            ([1, 2, 2, None, 3, 3, None], True),
            ([9, -42, -42, None, 76, 76, None], True),
        ],
    )
    def test_is_symmetric(self, root_list: list[int | None], expected: bool):
        result = run_is_symmetric(Solution, root_list)
        assert_is_symmetric(result, expected)
