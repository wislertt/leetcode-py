def run_shortest_word_distance_iii(
    solution_class: type, words_dict: list[str], word1: str, word2: str
):
    implementation = solution_class()
    return implementation.shortest_word_distance(words_dict, word1, word2)


def assert_shortest_word_distance_iii(result: int, expected: int) -> bool:
    assert result == expected
    return True
