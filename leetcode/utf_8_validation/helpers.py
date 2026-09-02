def run_valid_utf8(solution_class: type, data: list[int]):
    implementation = solution_class()
    return implementation.valid_utf8(data)


def assert_valid_utf8(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
