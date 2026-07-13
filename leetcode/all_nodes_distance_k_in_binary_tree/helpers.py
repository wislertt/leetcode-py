from leetcode_py import TreeNode


def run_distance_k(solution_class: type, root_list: list[int | None], target: int, k: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.distance_k(root, target, k)


def assert_distance_k(result: list[int], expected: list[int]) -> bool:
    # Order does not matter; sort both sides for comparison
    assert sorted(result) == sorted(expected)
    return True
