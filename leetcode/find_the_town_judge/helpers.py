def run_find_judge(solution_class: type, n: int, trust: list[list[int]]):
    implementation = solution_class()
    return implementation.find_judge(n, trust)


def assert_find_judge(result: int, expected: int) -> bool:
    assert result == expected
    return True
