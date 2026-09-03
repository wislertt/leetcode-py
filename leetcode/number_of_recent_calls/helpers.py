def run_recent_counter(solution_class: type, operations: list[str], inputs: list[list[int]]):
    counter = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "RecentCounter":
            counter = solution_class()
            results.append(None)
        elif op == "ping" and counter is not None:
            results.append(counter.ping(inputs[i][0]))
    return results, counter


def assert_recent_counter(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
