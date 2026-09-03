def run_distinct_subseq_ii(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.distinct_subseq_ii(s)


def assert_distinct_subseq_ii(result: int, expected: int) -> bool:
    assert result == expected
    return True
