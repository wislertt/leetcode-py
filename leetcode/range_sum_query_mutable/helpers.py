def run_num_array(solution_class: type, operations: list[str], inputs: list[list]):
    num_array = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "NumArray":
            num_array = solution_class(inputs[i][0])
            results.append(None)
        elif op == "update" and num_array is not None:
            num_array.update(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "sum_range" and num_array is not None:
            results.append(num_array.sum_range(inputs[i][0], inputs[i][1]))
    return results, num_array


def assert_num_array(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
