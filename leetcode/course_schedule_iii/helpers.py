def run_schedule_course(solution_class: type, courses: list[list[int]]):
    implementation = solution_class()
    return implementation.schedule_course(courses)


def assert_schedule_course(result: int, expected: int) -> bool:
    assert result == expected
    return True
