def run_num_matching_subseq(solution_class: type, s: str, words: list[str]):
    implementation = solution_class()
    return implementation.num_matching_subseq(s, words)


def assert_num_matching_subseq(result: int, expected: int) -> bool:
    assert result == expected
    return True
