def run_bulb_switch(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.bulb_switch(n)


def assert_bulb_switch(result: int, expected: int) -> bool:
    assert result == expected
    return True
