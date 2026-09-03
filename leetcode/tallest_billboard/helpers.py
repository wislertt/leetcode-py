def run_tallest_billboard(solution_class: type, rods: list[int]):
    implementation = solution_class()
    return implementation.tallest_billboard(rods)


def assert_tallest_billboard(result: int, expected: int) -> bool:
    assert result == expected
    return True
