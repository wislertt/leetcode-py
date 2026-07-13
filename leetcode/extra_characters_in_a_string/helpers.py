def run_min_extra_char(solution_class: type, s: str, dictionary: list[str]):
    implementation = solution_class()
    return implementation.min_extra_char(s, dictionary)


def assert_min_extra_char(result: int, expected: int) -> bool:
    assert result == expected
    return True
