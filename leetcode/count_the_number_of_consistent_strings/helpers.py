def run_count_consistent_strings(solution_class: type, allowed: str, words: list[str]):
    implementation = solution_class()
    return implementation.count_consistent_strings(allowed, words)


def assert_count_consistent_strings(result: int, expected: int) -> bool:
    assert result == expected
    return True
