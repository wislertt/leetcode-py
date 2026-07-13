def run_check_if_prerequisite(
    solution_class: type, num_courses: int, prerequisites: list[list[int]], queries: list[list[int]]
):
    implementation = solution_class()
    return implementation.check_if_prerequisite(num_courses, prerequisites, queries)


def assert_check_if_prerequisite(result: list[bool], expected: list[bool]) -> bool:
    assert result == expected
    return True
