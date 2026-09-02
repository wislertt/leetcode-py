import pytest

from leetcode_py import logged_test

from .helpers import assert_serialize_deserialize_n_ary, run_serialize_deserialize_n_ary
from .solution import Codec


class TestSerializeAndDeserializeNAryTree:
    @logged_test
    @pytest.mark.parametrize(
        "root_list",
        [
            ([1, None, 3, 2, 4, None, 5, 6]),
            (
                [
                    1,
                    None,
                    2,
                    3,
                    4,
                    5,
                    None,
                    None,
                    6,
                    7,
                    None,
                    8,
                    None,
                    9,
                    10,
                    None,
                    None,
                    11,
                    None,
                    12,
                    None,
                    13,
                    None,
                    None,
                    14,
                ]
            ),
            ([]),
            ([1]),
            ([0]),
            ([1, None, 2, None, 3]),
            ([1, None, 2, 3, 4, 5, 6]),
            ([5, None, 9, None, 1, None, 8]),
            ([3, None, 7, 2, None, 0, 6, None, 4]),
            ([10, None, 1, 2, 3, None, None, 4, 5, None, 6, 7, 8, 9, 10]),
            ([2, None, 1, None, 3, None, 4, None, 5, None, 6]),
            ([4, None, 2, 6, None, None, 1, 5, 7]),
        ],
    )
    def test_serialize_deserialize_n_ary(self, root_list: list[int | None]):
        result = run_serialize_deserialize_n_ary(Codec, root_list)
        assert_serialize_deserialize_n_ary(result, root_list)
