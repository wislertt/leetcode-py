def run_add_strings(solution_class: type, num1: str, num2: str):
    implementation = solution_class()
    return implementation.add_strings(num1, num2)


def assert_add_strings(result: str, expected: str) -> bool:
    assert result == expected
    return True
