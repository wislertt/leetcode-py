def run_unique_morse_representations(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.unique_morse_representations(words)


def assert_unique_morse_representations(result: int, expected: int) -> bool:
    assert result == expected
    return True
