def run_plus_one(solution_class: type, digits: list[int]):
    implementation = solution_class()
    return implementation.plus_one(digits)


def assert_plus_one(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
