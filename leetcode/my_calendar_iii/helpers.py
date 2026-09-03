def run_calendar_ops(solution_class: type, operations: list[str], inputs: list[list[int]]):
    calendar = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "MyCalendarThree":
            calendar = solution_class()
            results.append(None)
        elif op == "book" and calendar is not None:
            results.append(calendar.book(inputs[i][0], inputs[i][1]))
    return results, calendar


def assert_calendar_ops(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
