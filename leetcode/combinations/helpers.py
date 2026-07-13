def run_combine(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.combine(n, k)


def assert_combine(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert sorted([tuple(p) for p in result]) == sorted([tuple(p) for p in expected])
    return True
