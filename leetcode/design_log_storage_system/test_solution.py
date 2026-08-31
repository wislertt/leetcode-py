import pytest

from leetcode_py import logged_test

from .helpers import assert_log_storage, run_log_storage
from .solution import LogSystem


class TestDesignLogStorageSystem:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["LogSystem", "put", "put", "put", "retrieve", "retrieve"],
                [
                    [],
                    [1, "2017:01:01:23:59:59"],
                    [2, "2017:01:01:22:59:59"],
                    [3, "2016:01:01:00:00:00"],
                    ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"],
                    ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"],
                ],
                [None, None, None, None, [1, 2, 3], [1, 2]],
            ),
            (
                ["LogSystem", "put", "retrieve"],
                [
                    [],
                    [1, "2017:01:01:00:00:00"],
                    ["2017:01:01:00:00:00", "2017:01:01:00:00:00", "Second"],
                ],
                [None, None, [1]],
            ),
            (
                ["LogSystem", "put", "put", "retrieve", "retrieve"],
                [
                    [],
                    [5, "2015:06:15:12:30:45"],
                    [7, "2015:06:15:12:30:45"],
                    ["2015:06:15:12:30:45", "2015:06:15:12:30:45", "Second"],
                    ["2015:01:01:00:00:00", "2015:12:31:23:59:59", "Year"],
                ],
                [None, None, None, [5, 7], [5, 7]],
            ),
            (
                ["LogSystem", "put", "put", "retrieve", "retrieve", "retrieve"],
                [
                    [],
                    [10, "2017:12:31:23:59:59"],
                    [11, "2018:01:01:00:00:00"],
                    ["2017:01:01:00:00:00", "2017:12:31:23:59:59", "Year"],
                    ["2016:01:01:00:00:00", "2018:12:31:23:59:59", "Year"],
                    ["2017:12:01:00:00:00", "2018:01:31:23:59:59", "Month"],
                ],
                [None, None, None, [10], [10, 11], [10, 11]],
            ),
            (
                ["LogSystem", "put", "retrieve", "retrieve"],
                [
                    [],
                    [3, "2013:05:15:10:00:00"],
                    ["2013:05:15:10:00:00", "2013:05:15:10:00:00", "Second"],
                    ["2000:01:01:00:00:00", "2020:01:01:00:00:00", "Year"],
                ],
                [None, None, [3], [3]],
            ),
            (
                ["LogSystem", "put", "put", "retrieve"],
                [
                    [],
                    [1, "2010:01:01:00:00:00"],
                    [2, "2012:01:01:00:00:00"],
                    ["2011:01:01:00:00:00", "2011:01:01:00:00:00", "Second"],
                ],
                [None, None, None, []],
            ),
            (
                ["LogSystem", "put", "put", "retrieve", "retrieve"],
                [
                    [],
                    [1, "2000:01:01:00:00:00"],
                    [2, "2000:01:02:00:00:00"],
                    ["2000:01:01:00:00:00", "2000:01:02:23:59:59", "Day"],
                    ["2000:01:01:00:00:00", "2000:01:02:23:59:59", "Hour"],
                ],
                [None, None, None, [1, 2], [1, 2]],
            ),
            (
                ["LogSystem", "put", "retrieve", "retrieve", "retrieve", "retrieve"],
                [
                    [],
                    [9, "2011:03:07:05:13:42"],
                    ["2011:03:07:05:13:42", "2011:03:07:05:13:42", "Minute"],
                    ["2011:03:07:05:13:42", "2011:03:07:05:13:42", "Hour"],
                    ["2011:03:07:05:13:42", "2011:03:07:05:13:41", "Minute"],
                    ["2011:03:07:05:13:42", "2011:03:07:05:13:41", "Second"],
                ],
                [None, None, [9], [9], [9], []],
            ),
            (
                ["LogSystem", "put", "put", "put", "retrieve"],
                [
                    [],
                    [1, "2005:03:05:00:00:00"],
                    [2, "2005:03:05:00:00:00"],
                    [3, "2004:03:05:00:00:00"],
                    ["2005:03:05:00:00:00", "2005:03:05:00:00:00", "Second"],
                ],
                [None, None, None, None, [1, 2]],
            ),
            (
                ["LogSystem", "put", "retrieve"],
                [
                    [],
                    [1, "2017:06:02:07:09:22"],
                    ["2017:06:02:07:09:21", "2017:06:02:07:09:22", "Second"],
                ],
                [None, None, [1]],
            ),
            (
                ["LogSystem", "put", "put", "retrieve", "retrieve"],
                [
                    [],
                    [1, "2000:01:01:00:00:00"],
                    [2, "1999:12:31:23:59:59"],
                    ["1999:12:31:23:59:59", "2000:01:01:00:00:00", "Second"],
                    ["1999:12:31:23:59:59", "2000:01:01:00:00:00", "Minute"],
                ],
                [None, None, None, [1, 2], [1, 2]],
            ),
            (
                ["LogSystem", "retrieve"],
                [[], ["2000:01:01:00:00:00", "2017:01:01:00:00:00", "Year"]],
                [None, []],
            ),
        ],
    )
    def test_log_storage(
        self, operations: list[str], inputs: list[list], expected: list[list[int] | None]
    ):
        result, _ = run_log_storage(LogSystem, operations, inputs)
        assert_log_storage(result, expected)
