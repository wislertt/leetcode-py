def run_get_order(solution_class: type, tasks: list[list[int]]):
    implementation = solution_class()
    return implementation.get_order(tasks)


def assert_get_order(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
