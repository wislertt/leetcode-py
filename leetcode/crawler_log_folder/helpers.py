def run_min_operations(solution_class: type, logs: list[str]):
    implementation = solution_class()
    return implementation.min_operations(logs)


def assert_min_operations(result: int, expected: int) -> bool:
    assert result == expected
    return True
