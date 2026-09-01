def run_count_students(solution_class: type, students: list[int], sandwiches: list[int]):
    implementation = solution_class()
    return implementation.count_students(students, sandwiches)


def assert_count_students(result: int, expected: int) -> bool:
    assert result == expected
    return True
