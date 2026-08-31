def run_kth_grammar(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.kth_grammar(n, k)


def assert_kth_grammar(result: int, expected: int) -> bool:
    assert result == expected
    return True
