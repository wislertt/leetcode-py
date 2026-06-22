def run_find_itinerary(solution_class: type, tickets: list[list[str]]):
    implementation = solution_class()
    return implementation.find_itinerary(tickets)


def assert_find_itinerary(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
