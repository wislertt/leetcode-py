def run_range_sum_query_2d_mutable(
    solution_class: type, operations: list[str], inputs: list[list[list[int]]]
):
    matrix_obj = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "NumMatrix":
            matrix_obj = solution_class(inputs[i][0])
            results.append(None)
        elif op == "update" and matrix_obj is not None:
            matrix_obj.update(inputs[i][0], inputs[i][1], inputs[i][2])
            results.append(None)
        elif op == "sum_region" and matrix_obj is not None:
            results.append(
                matrix_obj.sum_region(inputs[i][0], inputs[i][1], inputs[i][2], inputs[i][3])
            )
    return results, matrix_obj


def assert_range_sum_query_2d_mutable(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
