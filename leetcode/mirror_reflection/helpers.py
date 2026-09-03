def run_mirror_reflection(solution_class: type, p: int, q: int):
    implementation = solution_class()
    return implementation.mirror_reflection(p, q)


def assert_mirror_reflection(result: int, expected: int) -> bool:
    assert result == expected
    return True
