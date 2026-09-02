def run_score_of_string(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.score_of_string(s)


def assert_score_of_string(result: int, expected: int) -> bool:
    assert result == expected
    return True
