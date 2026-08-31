import pytest

from leetcode_py import logged_test

from .helpers import assert_num_music_playlists, run_num_music_playlists
from .solution import Solution


class TestNumberOfMusicPlaylists:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, goal, k, expected",
        [
            (3, 3, 1, 6),
            (2, 3, 0, 6),
            (2, 3, 1, 2),
            (1, 1, 0, 1),
            (1, 5, 0, 1),
            (2, 2, 1, 2),
            (2, 2, 0, 2),
            (3, 4, 1, 18),
            (3, 4, 0, 36),
            (4, 4, 2, 24),
            (3, 5, 1, 42),
            (2, 5, 1, 2),
            (4, 6, 2, 168),
            (5, 7, 2, 3000),
            (10, 12, 3, 676505593),
            (2, 100, 1, 2),
            (100, 100, 0, 437918130),
            (16, 16, 4, 789741546),
        ],
    )
    def test_num_music_playlists(self, n: int, goal: int, k: int, expected: int):
        result = run_num_music_playlists(Solution, n, goal, k)
        assert_num_music_playlists(result, expected)
