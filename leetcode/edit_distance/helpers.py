def run_min_distance(solution_class: type, word1: str, word2: str):
    implementation = solution_class()
    return implementation.min_distance(word1, word2)


def assert_min_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
