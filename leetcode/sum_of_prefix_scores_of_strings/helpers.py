def run_sum_prefix_scores(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.sum_prefix_scores(words)


def assert_sum_prefix_scores(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
