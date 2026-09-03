def run_to_lower_case(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.to_lower_case(s)


def assert_to_lower_case(result: str, expected: str) -> bool:
    assert result == expected
    return True
