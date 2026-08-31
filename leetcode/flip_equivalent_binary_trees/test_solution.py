import pytest

from leetcode_py import logged_test

from .helpers import assert_flip_equiv, run_flip_equiv
from .solution import Solution


class TestFlipEquivalentBinaryTrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root1_list, root2_list, expected",
        [
            (
                [1, 2, 3, 4, 5, 6, None, None, None, 7, 8],
                [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7],
                True,
            ),
            ([], [], True),
            ([], [1], False),
            ([1], [], False),
            ([1], [1], True),
            ([1], [2], False),
            ([1, 2], [1, None, 2], True),
            ([1, 2], [2, 1], False),
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2, 3], [1, 3, 2], True),
            ([1, 2, 3, 4], [1, 3, 2, None, 4], False),
            ([1, 2, 3, 4], [1, 3, 2, 4], False),
            ([5, 3, 8, 1, 4], [5, 8, 3, None, None, 4, 1], True),
        ],
    )
    def test_flip_equiv(
        self, root1_list: list[int | None], root2_list: list[int | None], expected: bool
    ):
        result = run_flip_equiv(Solution, root1_list, root2_list)
        assert_flip_equiv(result, expected)
