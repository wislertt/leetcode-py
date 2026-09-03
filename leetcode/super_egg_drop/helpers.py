def run_super_egg_drop(solution_class: type, k: int, n: int):
    implementation = solution_class()
    return implementation.super_egg_drop(k, n)


def assert_super_egg_drop(result: int, expected: int) -> bool:
    assert result == expected
    return True
