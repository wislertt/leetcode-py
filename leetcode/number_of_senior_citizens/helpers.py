def run_count_seniors(solution_class: type, details: list[str]):
    implementation = solution_class()
    return implementation.count_seniors(details)


def assert_count_seniors(result: int, expected: int) -> bool:
    assert result == expected
    return True
