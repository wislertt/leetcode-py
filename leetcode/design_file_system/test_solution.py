import pytest

from leetcode_py import logged_test

from .helpers import assert_file_system, run_file_system
from .solution import FileSystem


class TestDesignFileSystem:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["FileSystem", "createPath", "get"], [[], ["/a", 1], ["/a"]], [None, True, 1]),
            (
                ["FileSystem", "createPath", "createPath", "get", "createPath", "get"],
                [[], ["/leet", 1], ["/leet/code", 2], ["/leet/code"], ["/c/d", 1], ["/c"]],
                [None, True, True, 2, False, -1],
            ),
            (["FileSystem", "createPath", "get"], [[], ["/a", 5], ["/b"]], [None, True, -1]),
            (
                ["FileSystem", "createPath", "createPath", "get"],
                [[], ["/a", 1], ["/a", 2], ["/a"]],
                [None, True, False, 1],
            ),
            (
                ["FileSystem", "createPath", "createPath", "createPath", "get", "get", "get"],
                [[], ["/a", 1], ["/a/b", 2], ["/a/b/c", 3], ["/a"], ["/a/b"], ["/a/b/c"]],
                [None, True, True, True, 1, 2, 3],
            ),
            (
                ["FileSystem", "createPath", "get"],
                [[], ["/a/b/c/d", 9], ["/a/b/c/d"]],
                [None, False, -1],
            ),
            (
                ["FileSystem", "createPath", "createPath", "get", "get"],
                [[], ["/x", 1], ["/x/y/z", 7], ["/x/y"], ["/x/y/z"]],
                [None, True, False, -1, -1],
            ),
            (
                [
                    "FileSystem",
                    "createPath",
                    "createPath",
                    "createPath",
                    "createPath",
                    "get",
                    "get",
                    "get",
                ],
                [[], ["/a", 1], ["/b", 2], ["/a/x", 3], ["/b/y", 4], ["/a/x"], ["/b/y"], ["/a/y"]],
                [None, True, True, True, True, 3, 4, -1],
            ),
            (
                ["FileSystem", "createPath", "createPath", "createPath", "get", "get"],
                [[], ["/c/d", 1], ["/c", 2], ["/c/d", 3], ["/c"], ["/c/d"]],
                [None, False, True, True, 2, 3],
            ),
            (["FileSystem", "createPath", "get"], [[], ["/min", 1], ["/min"]], [None, True, 1]),
            (
                ["FileSystem", "createPath", "get"],
                [[], ["/max", 1000000000], ["/max"]],
                [None, True, 1000000000],
            ),
            (
                ["FileSystem", "createPath", "createPath", "get", "get", "get"],
                [[], ["/ab", 1], ["/ab/cd", 2], ["/ab"], ["/ab/cd"], ["/a"]],
                [None, True, True, 1, 2, -1],
            ),
            (
                [
                    "FileSystem",
                    "createPath",
                    "createPath",
                    "createPath",
                    "get",
                    "get",
                    "createPath",
                    "get",
                ],
                [
                    [],
                    ["/a", 1],
                    ["/a", 1],
                    ["/a/b/c", 1],
                    ["/a/b"],
                    ["/a/b/c"],
                    ["/a/b", 2],
                    ["/a/b"],
                ],
                [None, True, False, False, -1, -1, True, 2],
            ),
            (
                ["FileSystem", "createPath", "createPath", "createPath", "get", "get"],
                [[], ["/p", 1], ["/p/q", 2], ["/p", 3], ["/p"], ["/p/q"]],
                [None, True, True, False, 1, 2],
            ),
        ],
    )
    def test_file_system(
        self, operations: list[str], inputs: list[list], expected: list[bool | int | None]
    ):
        result, _ = run_file_system(FileSystem, operations, inputs)
        assert_file_system(result, expected)
