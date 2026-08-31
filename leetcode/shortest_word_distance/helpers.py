def run_shortest_distance(solution_class: type, words_dict: list[str], word1: str, word2: str):
    implementation = solution_class()
    return implementation.shortest_distance(words_dict, word1, word2)


def assert_shortest_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
