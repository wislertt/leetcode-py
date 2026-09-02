import pytest

from leetcode_py import logged_test

from .helpers import assert_round_trip, assert_round_trip_count, run_serialize_deserialize
from .solution import Codec


class TestSerializeAndDeserializeBst:
    @logged_test
    @pytest.mark.parametrize(
        "root_list",
        [
            ([]),
            ([1]),
            ([2, 1, 3]),
            ([0]),
            ([10000]),
            ([5, 3, 6, 2, 4, None, None, 1]),
            ([10, 5, 15, 3, 7, 12, 18]),
            ([10, 5, 15, 3, 7, None, 18]),
            ([1, None, 2, None, 3, None, 4]),
            ([4, 3, None, 2, None, 1]),
            ([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]),
            ([1000, 500, 1500, 250, 750, 1250, 1750]),
            ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
            ([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 17]),
            ([3431, 3131, 6331, 2038, None, 3499, 9852, None, None, None, None, 9505]),
            ([6302, 1777, None, 545, 3174]),
            ([7123, 3946, 8534, 1215, 4033, None, 9882, None, None, None, None, 9104]),
            ([9071, None, 9185]),
        ],
    )
    def test_serialize_deserialize(self, root_list: list[int | None]):
        result = run_serialize_deserialize(Codec, root_list)
        assert_round_trip(result, root_list)

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_count",
        [
            ([], 0),
            ([1], 1),
            ([2, 1, 3], 3),
            ([0], 1),
            ([10000], 1),
            ([5, 3, 6, 2, 4, None, None, 1], 6),
            ([10, 5, 15, 3, 7, 12, 18], 7),
            ([10, 5, 15, 3, 7, None, 18], 6),
            ([1, None, 2, None, 3, None, 4], 4),
        ],
    )
    def test_serialize_deserialize_node_count(
        self, root_list: list[int | None], expected_count: int
    ):
        result = run_serialize_deserialize(Codec, root_list)
        assert_round_trip_count(result, expected_count)
