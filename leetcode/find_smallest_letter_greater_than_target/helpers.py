def run_next_greatest_letter(solution_class: type, letters: list[str], target: str):
    implementation = solution_class()
    return implementation.next_greatest_letter(letters, target)


def assert_next_greatest_letter(result: str, expected: str) -> bool:
    assert result == expected
    return True
