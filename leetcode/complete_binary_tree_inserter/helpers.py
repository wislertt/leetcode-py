from leetcode_py import TreeNode


def run_complete_binary_tree_inserter(
    solution_class: type, operations: list[str], inputs: list[list[int | None]]
):
    inserter = None
    results: list[int | list[int | None] | None] = []
    for i, op in enumerate(operations):
        if op == "CBTInserter":
            root = TreeNode[int].from_list(inputs[i])
            assert root is not None
            inserter = solution_class(root)
            results.append(None)
        elif op == "insert" and inserter is not None:
            val = inputs[i][0]
            assert val is not None
            results.append(inserter.insert(val))
        elif op == "get_root" and inserter is not None:
            current_root = inserter.get_root()
            assert current_root is not None
            results.append(current_root.to_list())
    return results, inserter


def assert_complete_binary_tree_inserter(
    result: list[int | list[int | None] | None], expected: list[int | list[int | None] | None]
) -> bool:
    assert result == expected
    return True
