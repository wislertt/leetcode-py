from leetcode_py import TreeNode


def run_pseudo_palindromic_paths(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.pseudo_palindromic_paths(root)


def assert_pseudo_palindromic_paths(result: int, expected: int) -> bool:
    assert result == expected
    return True
