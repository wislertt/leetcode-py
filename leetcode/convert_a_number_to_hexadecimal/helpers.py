def run_to_hex(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.to_hex(num)


def assert_to_hex(result: str, expected: str) -> bool:
    assert result == expected
    return True
