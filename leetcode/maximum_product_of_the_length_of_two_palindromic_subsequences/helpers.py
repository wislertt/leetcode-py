def run_max_product(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.max_product(s)


def assert_max_product(result: int, expected: int) -> bool:
    assert result == expected
    return True
