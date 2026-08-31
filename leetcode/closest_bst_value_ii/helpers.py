from leetcode_py import TreeNode


def run_closest_k_values(solution_class: type, root_list: list[int | None], target: float, k: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.closest_k_values(root, target, k)


def assert_closest_k_values(result: list[int], expected: list[int]) -> bool:
    # Sort both result and expected for order-independent comparison
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
