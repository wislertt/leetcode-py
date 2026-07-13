def run_merge_alternately(solution_class: type, word1: str, word2: str):
    implementation = solution_class()
    return implementation.merge_alternately(word1, word2)


def assert_merge_alternately(result: str, expected: str) -> bool:
    assert result == expected
    return True
