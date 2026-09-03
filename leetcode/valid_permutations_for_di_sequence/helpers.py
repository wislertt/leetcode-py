def run_num_perms_di_sequence(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.num_perms_di_sequence(s)


def assert_num_perms_di_sequence(result: int, expected: int) -> bool:
    assert result == expected
    return True
