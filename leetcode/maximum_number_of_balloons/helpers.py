def run_max_number_of_balloons(solution_class: type, text: str):
    implementation = solution_class()
    return implementation.max_number_of_balloons(text)


def assert_max_number_of_balloons(result: int, expected: int) -> bool:
    assert result == expected
    return True
