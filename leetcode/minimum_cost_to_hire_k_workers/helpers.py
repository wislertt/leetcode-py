def run_mincost_to_hire_workers(solution_class: type, quality: list[int], wage: list[int], k: int):
    implementation = solution_class()
    return implementation.mincost_to_hire_workers(quality, wage, k)


def assert_mincost_to_hire_workers(result: float, expected: float) -> bool:
    # The statement accepts answers within 10^-5 of the actual answer
    assert abs(result - expected) < 1e-5
    return True
