import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_utf8, run_valid_utf8
from .solution import Solution


class TestUtf8Validation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "data, expected",
        [
            ([197, 130, 1], True),
            ([235, 140, 4], False),
            ([1], True),
            ([0], True),
            ([127], True),
            ([128], False),
            ([255], False),
            ([247], False),
            ([194, 130], True),
            ([224, 160, 128], True),
            ([240, 144, 128, 128], True),
            ([194], False),
            ([194, 129, 1], True),
            ([145], False),
            ([230, 136], False),
            ([248, 130, 130, 130, 130], False),
            ([240, 130, 130, 130], True),
            ([240, 144, 128], False),
            ([197, 130, 1, 194, 130], True),
            ([1, 194, 130, 224, 160, 128], True),
        ],
    )
    def test_valid_utf8(self, data: list[int], expected: bool):
        result = run_valid_utf8(Solution, data)
        assert_valid_utf8(result, expected)
