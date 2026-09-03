from leetcode_py import TreeNode


def run_min_camera_cover(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.min_camera_cover(root)


def assert_min_camera_cover(result: int, expected: int) -> bool:
    assert result == expected
    return True
