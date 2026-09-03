def run_powerful_integers(solution_class: type, x: int, y: int, bound: int):
    implementation = solution_class()
    return implementation.powerful_integers(x, y, bound)


def assert_powerful_integers(result: list[int], expected: list[int]) -> bool:
    # Order does not matter; sort both sides for comparison
    assert sorted(result) == sorted(expected)
    return True
