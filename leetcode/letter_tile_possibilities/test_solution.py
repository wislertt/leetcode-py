import pytest

from leetcode_py import logged_test

from .helpers import assert_num_tile_possibilities, run_num_tile_possibilities
from .solution import Solution


class TestLetterTilePossibilities:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "tiles, expected",
        [
            ("AAB", 8),
            ("AAABBC", 188),
            ("V", 1),
            ("A", 1),
            ("AA", 2),
            ("AB", 4),
            ("AAA", 3),
            ("ABC", 15),
            ("AABB", 18),
            ("AAABB", 33),
            ("ZZZZZZZ", 7),
            ("ABCC", 34),
            ("QQQ", 3),
            ("ABCDEFG", 13699),
        ],
    )
    def test_num_tile_possibilities(self, tiles: str, expected: int):
        result = run_num_tile_possibilities(Solution, tiles)
        assert_num_tile_possibilities(result, expected)
