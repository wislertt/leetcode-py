def run_max_performance(
    solution_class: type, n: int, speed: list[int], efficiency: list[int], k: int
):
    implementation = solution_class()
    return implementation.max_performance(n, speed, efficiency, k)


def assert_max_performance(result: int, expected: int) -> bool:
    assert result == expected
    return True
