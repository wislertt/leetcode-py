def run_confusing_number_ii(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.confusing_number_ii(n)


def assert_confusing_number_ii(result: int, expected: int) -> bool:
    assert result == expected
    return True
