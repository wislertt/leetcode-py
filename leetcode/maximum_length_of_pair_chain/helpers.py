def run_find_longest_chain(solution_class: type, pairs: list[list[int]]):
    implementation = solution_class()
    return implementation.find_longest_chain(pairs)


def assert_find_longest_chain(result: int, expected: int) -> bool:
    assert result == expected
    return True
