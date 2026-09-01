def run_number_of_ways(solution_class: type, num_people: int):
    implementation = solution_class()
    return implementation.number_of_ways(num_people)


def assert_number_of_ways(result: int, expected: int) -> bool:
    assert result == expected
    return True
