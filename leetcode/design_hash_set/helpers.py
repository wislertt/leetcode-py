def run_hash_set(solution_class: type, operations: list[str], inputs: list[list[int]]):
    hash_set = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "MyHashSet":
            hash_set = solution_class()
            results.append(None)
        elif op == "add" and hash_set is not None:
            hash_set.add(inputs[i][0])
            results.append(None)
        elif op == "remove" and hash_set is not None:
            hash_set.remove(inputs[i][0])
            results.append(None)
        elif op == "contains" and hash_set is not None:
            results.append(hash_set.contains(inputs[i][0]))
    return results, hash_set


def assert_hash_set(result: list[int | bool | None], expected: list[int | bool | None]) -> bool:
    assert result == expected
    return True
