def run_network_delay_time(solution_class: type, times: list[list[int]], n: int, k: int):
    implementation = solution_class()
    return implementation.network_delay_time(times, n, k)


def assert_network_delay_time(result: int, expected: int) -> bool:
    assert result == expected
    return True
