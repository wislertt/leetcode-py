def run_is_interleave(solution_class: type, s1: str, s2: str, s3: str):
    implementation = solution_class()
    return implementation.is_interleave(s1, s2, s3)


def assert_is_interleave(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
