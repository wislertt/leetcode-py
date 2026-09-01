def run_most_points(solution_class: type, questions: list[list[int]]):
    implementation = solution_class()
    return implementation.most_points(questions)


def assert_most_points(result: int, expected: int) -> bool:
    assert result == expected
    return True
