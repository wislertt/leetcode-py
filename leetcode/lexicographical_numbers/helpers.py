def run_lexical_order(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.lexical_order(n)


def assert_lexical_order(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
