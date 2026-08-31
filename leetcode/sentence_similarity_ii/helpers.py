def run_are_sentences_similar_two(
    solution_class: type, sentence1: list[str], sentence2: list[str], similar_pairs: list[list[str]]
):
    implementation = solution_class()
    return implementation.are_sentences_similar_two(sentence1, sentence2, similar_pairs)


def assert_are_sentences_similar_two(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
