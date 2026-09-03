def run_is_long_pressed_name(solution_class: type, name: str, typed: str):
    implementation = solution_class()
    return implementation.is_long_pressed_name(name, typed)


def assert_is_long_pressed_name(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
