def run_letter_case_permutation(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.letter_case_permutation(s)


def assert_letter_case_permutation(result: list[str], expected: list[str]) -> bool:
    result.sort()
    expected.sort()
    assert result == expected
    return True
