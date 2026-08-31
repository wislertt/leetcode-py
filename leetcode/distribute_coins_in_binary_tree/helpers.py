from leetcode_py import TreeNode


def run_distribute_coins(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.distribute_coins(root)


def assert_distribute_coins(result: int, expected: int) -> bool:
    assert result == expected
    return True
