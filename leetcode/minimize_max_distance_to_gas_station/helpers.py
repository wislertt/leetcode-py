def run_minmax_gas_dist(solution_class: type, stations: list[int], k: int):
    implementation = solution_class()
    return implementation.minmax_gas_dist(stations, k)


def assert_minmax_gas_dist(result: float, expected: float) -> bool:
    assert abs(result - expected) < 10**-4
    return True
