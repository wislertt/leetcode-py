def run_find_maximized_capital(
    solution_class: type, k: int, w: int, profits: list[int], capital: list[int]
):
    implementation = solution_class()
    return implementation.find_maximized_capital(k, w, profits, capital)


def assert_find_maximized_capital(result: int, expected: int) -> bool:
    assert result == expected
    return True
