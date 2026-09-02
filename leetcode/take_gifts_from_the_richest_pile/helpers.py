def run_pick_gifts(solution_class: type, gifts: list[int], k: int):
    implementation = solution_class()
    return implementation.pick_gifts(gifts, k)


def assert_pick_gifts(result: int, expected: int) -> bool:
    assert result == expected
    return True
