def run_racecar(solution_class: type, target: int):
    implementation = solution_class()
    return implementation.racecar(target)


def assert_racecar(result: int, expected: int) -> bool:
    assert result == expected
    return True
