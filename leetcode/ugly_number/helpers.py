def run_is_ugly(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.is_ugly(n)


def assert_is_ugly(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
