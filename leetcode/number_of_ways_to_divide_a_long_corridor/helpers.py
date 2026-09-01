def run_number_of_ways(solution_class: type, corridor: str):
    implementation = solution_class()
    return implementation.number_of_ways(corridor)


def assert_number_of_ways(result: int, expected: int) -> bool:
    assert result == expected
    return True
