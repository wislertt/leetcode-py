from leetcode_py import TreeNode


def run_str2tree(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.str2tree(s)


def assert_str2tree(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
