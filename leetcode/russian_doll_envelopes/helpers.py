def run_max_envelopes(solution_class: type, envelopes: list[list[int]]):
    implementation = solution_class()
    return implementation.max_envelopes(envelopes)


def assert_max_envelopes(result: int, expected: int) -> bool:
    assert result == expected
    return True
