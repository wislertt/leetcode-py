def run_time_required_to_buy(solution_class: type, tickets: list[int], k: int):
    implementation = solution_class()
    return implementation.time_required_to_buy(tickets, k)


def assert_time_required_to_buy(result: int, expected: int) -> bool:
    assert result == expected
    return True
