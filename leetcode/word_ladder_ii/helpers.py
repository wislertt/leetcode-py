def run_find_ladders(solution_class: type, begin_word: str, end_word: str, word_list: list[str]):
    implementation = solution_class()
    return implementation.find_ladders(begin_word, end_word, word_list)


def assert_find_ladders(result: list[list[str]], expected: list[list[str]]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
