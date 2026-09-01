def run_find_the_winner(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.find_the_winner(n, k)


def assert_find_the_winner(result: int, expected: int) -> bool:
    assert result == expected
    return True
