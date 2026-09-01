def run_is_circular_sentence(solution_class: type, sentence: str):
    implementation = solution_class()
    return implementation.is_circular_sentence(sentence)


def assert_is_circular_sentence(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
