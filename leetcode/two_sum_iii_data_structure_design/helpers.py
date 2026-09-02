def run_two_sum(solution_class: type, operations: list[str], inputs: list[list[int]]):
    two_sum = None
    results: list[bool | None] = []
    for i, op in enumerate(operations):
        if op == "TwoSum":
            two_sum = solution_class()
            results.append(None)
        elif op == "add" and two_sum is not None:
            two_sum.add(inputs[i][0])
            results.append(None)
        elif op == "find" and two_sum is not None:
            results.append(two_sum.find(inputs[i][0]))
    return results, two_sum


def assert_two_sum(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
