def run_count_of_substrings(solution_class: type, word: str, k: int):
    implementation = solution_class()
    return implementation.count_of_substrings(word, k)


def assert_count_of_substrings(result: int, expected: int) -> bool:
    assert result == expected
    return True
