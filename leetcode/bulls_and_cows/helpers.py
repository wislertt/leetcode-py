def run_get_hint(solution_class: type, secret: str, guess: str):
    implementation = solution_class()
    return implementation.get_hint(secret, guess)


def assert_get_hint(result: str, expected: str) -> bool:
    assert result == expected
    return True
