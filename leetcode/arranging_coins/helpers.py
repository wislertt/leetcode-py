def run_arrange_coins(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.arrange_coins(n)


def assert_arrange_coins(result: int, expected: int) -> bool:
    assert result == expected
    return True
