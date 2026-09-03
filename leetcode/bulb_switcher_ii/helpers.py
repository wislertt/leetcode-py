def run_flip_lights(solution_class: type, n: int, presses: int):
    implementation = solution_class()
    return implementation.flip_lights(n, presses)


def assert_flip_lights(result: int, expected: int) -> bool:
    assert result == expected
    return True
