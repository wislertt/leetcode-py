def run_remove_duplicates(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.remove_duplicates(s, k)


def assert_remove_duplicates(result: str, expected: str) -> bool:
    assert result == expected
    return True
