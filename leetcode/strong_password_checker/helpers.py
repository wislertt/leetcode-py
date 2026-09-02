def run_strong_password_checker(solution_class: type, password: str):
    implementation = solution_class()
    return implementation.strong_password_checker(password)


def assert_strong_password_checker(result: int, expected: int) -> bool:
    assert result == expected
    return True
