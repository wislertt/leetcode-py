def run_employee_free_time(solution_class: type, schedule: list[list[list[int]]]):
    implementation = solution_class()
    return implementation.employee_free_time(schedule)


def assert_employee_free_time(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
