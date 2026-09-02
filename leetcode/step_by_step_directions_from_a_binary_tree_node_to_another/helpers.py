from leetcode_py import TreeNode


def run_get_directions(
    solution_class: type, root_list: list[int | None], start_value: int, dest_value: int
):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.get_directions(root, start_value, dest_value)


def assert_get_directions(result: str, expected: str) -> bool:
    assert result == expected
    return True
