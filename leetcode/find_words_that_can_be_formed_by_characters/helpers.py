def run_count_characters(solution_class: type, words: list[str], chars: str):
    implementation = solution_class()
    return implementation.count_characters(words, chars)


def assert_count_characters(result: int, expected: int) -> bool:
    assert result == expected
    return True
