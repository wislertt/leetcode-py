def run_minimum_length_encoding(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.minimum_length_encoding(words)


def assert_minimum_length_encoding(result: int, expected: int) -> bool:
    assert result == expected
    return True
