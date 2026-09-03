def run_to_goat_latin(solution_class: type, sentence: str):
    implementation = solution_class()
    return implementation.to_goat_latin(sentence)


def assert_to_goat_latin(result: str, expected: str) -> bool:
    assert result == expected
    return True
