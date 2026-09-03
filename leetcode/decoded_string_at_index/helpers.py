def run_decode_at_index(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.decode_at_index(s, k)


def assert_decode_at_index(result: str, expected: str) -> bool:
    assert result == expected
    return True
