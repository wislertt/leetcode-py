import pytest

from leetcode_py import logged_test

from .helpers import assert_length_longest_path, run_length_longest_path
from .solution import Solution


class TestLongestAbsoluteFilePath:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20),
            ("a", 0),
            ("file.txt", 8),
            ("dir\n\tf.txt", 9),
            ("a\n\tb\n\t\tc.txt", 9),
            ("a\n\tb.txt\n\tc", 7),
            ("a\n\tb\n\t\tc\n\t\t\td.txt", 11),
            ("dir\n\tsub\n\t\tfile with space.txt", 27),
            ("a\n\tb\n\t\tc.txt\n\t\t d.txt", 10),
            ("a\n\tb\n\t\tc\n\t\t\td.ext\n\t\te.ext", 11),
            ("x\n\ty\n\t\tz\n\t\t\tlongest.name.here", 23),
            ("a\n\tb\n\tc\n\t\td.txt", 9),
            ("dir1\n\tdir2\n\t\tfile1.txt\n\tdir3", 19),
            ("z", 0),
            ("a\n\tb\n\t\tc\n\t\t\td\n\t\t\t\te.txt", 13),
            ("a\n\tb\n\t\tc.txt\n\td\n\t\te.txt", 9),
            ("aa\n\tbb\n\t\tcc.txt\n\tdd\n\t\tee.txt\n\t\tff\n\t\t\tg.txt", 14),
            ("a\n\tb\n\t\tc\n\t\t\td\n\t\t\t\te\n\t\t\t\t\tf.txt", 15),
        ],
    )
    def test_length_longest_path(self, input_str: str, expected: int):
        result = run_length_longest_path(Solution, input_str)
        assert_length_longest_path(result, expected)
