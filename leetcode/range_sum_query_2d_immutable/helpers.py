def run_num_matrix(solution_class: type, operations: list[str], inputs: list[list]):
    num_matrix = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "NumMatrix":
            num_matrix = solution_class(inputs[i][0])
            results.append(None)
        elif op == "sumRegion" and num_matrix is not None:
            args = inputs[i]
            results.append(num_matrix.sum_region(args[0], args[1], args[2], args[3]))
    return results, num_matrix


def assert_num_matrix(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
