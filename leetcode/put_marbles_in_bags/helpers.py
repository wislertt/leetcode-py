def run_put_marbles(solution_class: type, weights: list[int], k: int):
    implementation = solution_class()
    return implementation.put_marbles(weights, k)


def assert_put_marbles(result: int, expected: int) -> bool:
    assert result == expected
    return True
