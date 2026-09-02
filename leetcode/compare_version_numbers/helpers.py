def run_compare_version(solution_class: type, version1: str, version2: str):
    implementation = solution_class()
    return implementation.compare_version(version1, version2)


def assert_compare_version(result: int, expected: int) -> bool:
    assert result == expected
    return True
