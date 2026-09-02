def run_license_key_formatting(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.license_key_formatting(s, k)


def assert_license_key_formatting(result: str, expected: str) -> bool:
    assert result == expected
    return True
