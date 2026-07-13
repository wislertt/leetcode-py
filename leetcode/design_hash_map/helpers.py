def run_hash_map(solution_class: type, operations: list[str], inputs: list[list[int]]):
    hash_map = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "MyHashMap":
            hash_map = solution_class()
            results.append(None)
        elif op == "put" and hash_map is not None:
            hash_map.put(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "get" and hash_map is not None:
            results.append(hash_map.get(inputs[i][0]))
        elif op == "remove" and hash_map is not None:
            hash_map.remove(inputs[i][0])
            results.append(None)
    return results, hash_map


def assert_hash_map(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
