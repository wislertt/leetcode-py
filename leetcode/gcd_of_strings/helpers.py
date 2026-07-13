def run_gcd_of_strings(solution_class: type, str1: str, str2: str):
    implementation = solution_class()
    return implementation.gcd_of_strings(str1, str2)


def assert_gcd_of_strings(result: str, expected: str) -> bool:
    assert result == expected
    return True
