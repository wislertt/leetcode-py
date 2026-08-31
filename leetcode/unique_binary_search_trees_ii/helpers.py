from leetcode_py import TreeNode


def _to_lists(trees: list[TreeNode[int] | None]) -> list[list[int | None]]:
    return sorted((tree.to_list() for tree in trees if tree is not None), key=repr)


def run_generate_trees(solution_class: type, n: int):
    implementation = solution_class()
    return _to_lists(implementation.generate_trees(n))


def assert_generate_trees(
    result: list[list[int | None]], n: int, expected_tree: list[int | None]
) -> bool:
    assert expected_tree in result
    assert len(result) == len({repr(tree) for tree in result})
    catalan = 1
    for i in range(n):
        catalan = catalan * 2 * (2 * i + 1) // (i + 2)
    assert len(result) == catalan
    return True
