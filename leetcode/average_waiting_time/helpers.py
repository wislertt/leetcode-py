def run_average_waiting_time(solution_class: type, customers: list[list[int]]):
    implementation = solution_class()
    return implementation.average_waiting_time(customers)


def assert_average_waiting_time(result: float, expected: float) -> bool:
    assert abs(result - expected) < 1e-5
    return True
