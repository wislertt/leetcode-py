def run_longest_str_chain(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.longest_str_chain(words)


def assert_longest_str_chain(result: int, expected: int) -> bool:
    assert result == expected
    return True
