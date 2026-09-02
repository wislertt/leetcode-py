def run_find_lus_length(solution_class: type, strs: list[str]):
    implementation = solution_class()
    return implementation.find_lus_length(strs)


def assert_find_lus_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
