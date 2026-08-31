def run_excel_sum_formula(solution_class: type, operations: list[str], inputs: list[list]):
    excel = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "Excel":
            excel = solution_class(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "set" and excel is not None:
            excel.set(inputs[i][0], inputs[i][1], inputs[i][2])
            results.append(None)
        elif op == "get" and excel is not None:
            results.append(excel.get(inputs[i][0], inputs[i][1]))
        elif op == "sum" and excel is not None:
            results.append(excel.sum(inputs[i][0], inputs[i][1], inputs[i][2]))
    return results, excel


def assert_excel_sum_formula(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
