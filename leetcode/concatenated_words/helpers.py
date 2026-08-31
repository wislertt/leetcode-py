def run_find_all_concatenated_words_in_a_dict(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.find_all_concatenated_words_in_a_dict(words)


def assert_find_all_concatenated_words_in_a_dict(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
