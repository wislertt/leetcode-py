def run_best_closing_time(solution_class: type, customers: str):
    implementation = solution_class()
    return implementation.best_closing_time(customers)


def assert_best_closing_time(result: int, expected: int) -> bool:
    assert result == expected
    return True
