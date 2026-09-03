def run_soup_servings(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.soup_servings(n)


def assert_soup_servings(result: float, expected: float) -> bool:
    assert abs(result - expected) <= 1e-5
    return True
