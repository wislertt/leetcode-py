def run_total_fruit(solution_class: type, fruits: list[int]):
    implementation = solution_class()
    return implementation.total_fruit(fruits)


def assert_total_fruit(result: int, expected: int) -> bool:
    assert result == expected
    return True
