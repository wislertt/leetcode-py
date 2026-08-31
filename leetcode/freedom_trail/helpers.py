def run_find_rotate_steps(solution_class: type, ring: str, key: str):
    implementation = solution_class()
    return implementation.find_rotate_steps(ring, key)


def assert_find_rotate_steps(result: int, expected: int) -> bool:
    assert result == expected
    return True
