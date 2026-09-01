def run_count_unguarded(
    solution_class: type, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
):
    implementation = solution_class()
    return implementation.count_unguarded(m, n, guards, walls)


def assert_count_unguarded(result: int, expected: int) -> bool:
    assert result == expected
    return True
