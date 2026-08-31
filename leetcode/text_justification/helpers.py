def run_full_justify(solution_class: type, words: list[str], max_width: int):
    implementation = solution_class()
    return implementation.full_justify(words, max_width)


def assert_full_justify(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
