def run_maximum_candies(solution_class: type, candies: list[int], k: int):
    implementation = solution_class()
    return implementation.maximum_candies(candies, k)


def assert_maximum_candies(result: int, expected: int) -> bool:
    assert result == expected
    return True
