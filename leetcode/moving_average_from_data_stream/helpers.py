def run_moving_average(solution_class: type, operations: list[str], inputs: list[list[int]]):
    average = None
    results: list[float | None] = []
    for i, op in enumerate(operations):
        if op == "MovingAverage":
            average = solution_class(inputs[i][0])
            results.append(None)
        elif op == "next" and average is not None:
            results.append(average.next(inputs[i][0]))
    return results, average


def assert_moving_average(result: list[float | None], expected: list[float | None]) -> bool:
    assert result == expected
    return True
