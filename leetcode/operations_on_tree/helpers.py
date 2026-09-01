def run_operations_on_tree(solution_class: type, operations: list[str], inputs: list[list[int]]):
    tree = None
    results: list[bool | None] = []
    for i, op in enumerate(operations):
        if op == "LockingTree":
            tree = solution_class(inputs[i])
            results.append(None)
        elif op == "lock" and tree is not None:
            results.append(tree.lock(inputs[i][0], inputs[i][1]))
        elif op == "unlock" and tree is not None:
            results.append(tree.unlock(inputs[i][0], inputs[i][1]))
        elif op == "upgrade" and tree is not None:
            results.append(tree.upgrade(inputs[i][0], inputs[i][1]))
    return results, tree


def assert_operations_on_tree(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
