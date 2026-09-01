def run_minimized_maximum(solution_class: type, n: int, quantities: list[int]):
    implementation = solution_class()
    return implementation.minimized_maximum(n, quantities)


def assert_minimized_maximum(result: int, expected: int) -> bool:
    assert result == expected
    return True
