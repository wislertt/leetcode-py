from leetcode_py import TreeNode


def assert_round_trip_count(result: TreeNode[int] | None, expected_count: int) -> bool:
    def count(node: TreeNode[int] | None) -> int:
        if node is None:
            return 0
        return 1 + count(node.left) + count(node.right)

    assert count(result) == expected_count
    return True


def run_serialize_deserialize(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    codec = solution_class()
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    return deserialized


def assert_round_trip(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode[int].from_list(expected_list) if expected_list else None
    if expected is None:
        assert result is None
    else:
        assert result is not None
        assert result.to_list() == expected.to_list()
    return True
