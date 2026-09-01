def run_can_construct(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.can_construct(s, k)


def assert_can_construct(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
