import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_subfolders, run_remove_subfolders
from .solution import Solution


class TestRemoveSubFoldersFromTheFilesystemTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "folder, expected",
        [
            (["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"], ["/a", "/c/d", "/c/f"]),
            (["/a", "/a/b/c", "/a/b/d"], ["/a"]),
            (["/a/b/c", "/a/b/ca", "/a/b/d"], ["/a/b/c", "/a/b/ca", "/a/b/d"]),
            (["/a"], ["/a"]),
            (["/a", "/aa"], ["/a", "/aa"]),
            (["/a/b", "/a"], ["/a"]),
            (["/x", "/x/y", "/x/y/z", "/p", "/p/q"], ["/p", "/x"]),
            (["/ab", "/abc", "/abcd", "/a"], ["/a", "/ab", "/abc", "/abcd"]),
            (["/one", "/one/two", "/three", "/three/four"], ["/one", "/three"]),
            (["/c", "/c/d", "/c/d/e", "/c/f", "/c/f/g"], ["/c"]),
            (["/a/b/c", "/a/b/ca", "/a/b/d", "/a", "/a/b"], ["/a"]),
            (["/z/x/y", "/z/x", "/z", "/a/b", "/a"], ["/a", "/z"]),
            (["/q/rs", "/q/rs/t", "/q"], ["/q"]),
            (["/aa/bb", "/aa", "/aa/bb/cc", "/bb", "/bb/cc"], ["/aa", "/bb"]),
            (["/deep/nested/path", "/deep", "/deep/nested"], ["/deep"]),
            (["/f", "/f/g", "/f/g/h", "/e"], ["/e", "/f"]),
        ],
    )
    def test_remove_subfolders(self, folder: list[str], expected: list[str]):
        result = run_remove_subfolders(Solution, folder)
        assert_remove_subfolders(result, expected)
