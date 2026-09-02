def run_count_prefix_suffix_pairs(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.count_prefix_suffix_pairs(words)


def assert_count_prefix_suffix_pairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
