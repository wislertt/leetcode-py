def run_mask_pii(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.mask_pii(s)


def assert_mask_pii(result: str, expected: str) -> bool:
    assert result == expected
    return True
