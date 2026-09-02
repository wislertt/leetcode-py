def run_are_sentences_similar(solution_class: type, sentence1: str, sentence2: str):
    implementation = solution_class()
    return implementation.are_sentences_similar(sentence1, sentence2)


def assert_are_sentences_similar(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
