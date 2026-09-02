def run_take_characters(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.take_characters(s, k)


def assert_take_characters(result: int, expected: int) -> bool:
    assert result == expected
    return True
