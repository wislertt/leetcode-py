from leetcode_py import TreeNode


def run_binary_search_tree_iterator(
    solution_class: type, root_list: list[int | None], operations: list[str]
):
    root = TreeNode[int].from_list(root_list)
    iterator = solution_class(root)
    results: list[int | bool | None] = [None]
    for op in operations:
        if op == "next":
            results.append(iterator.next())
        elif op == "has_next":
            results.append(iterator.has_next())
    return results, iterator


def assert_binary_search_tree_iterator(
    result: list[int | bool | None], expected: list[int | bool | None]
) -> bool:
    assert result == expected
    return True
