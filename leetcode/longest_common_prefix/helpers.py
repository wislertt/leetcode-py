def run_longest_common_prefix(solution_class: type, strs: list[str]):
    implementation = solution_class()
    return implementation.longest_common_prefix(strs)


def assert_longest_common_prefix(result: str, expected: str) -> bool:
    assert result == expected
    return True
