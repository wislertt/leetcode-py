from leetcode_py import TreeNode


def assert_all_possible_fbt_solution_count(
    result: list[TreeNode[int] | None], expected: int
) -> bool:
    assert len(result) == expected
    return True


def run_all_possible_fbt(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.all_possible_fbt(n)


def assert_all_possible_fbt(
    result: list[TreeNode[int] | None], expected: list[list[int | None]]
) -> bool:
    # Trees serialize to lists; compare as multisets since order doesn't matter
    roots = [tree for tree in result if tree is not None]
    assert len(roots) == len(result)

    def key(tree: list[int | None]) -> tuple[int, str]:
        return (len(tree), str(tree))

    result_lists = [tree.to_list() for tree in roots]
    assert sorted(result_lists, key=key) == sorted(expected, key=key)
    return True
