def run_num_ways(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.num_ways(n, k)


def assert_num_ways(result: int, expected: int) -> bool:
    assert result == expected
    return True
