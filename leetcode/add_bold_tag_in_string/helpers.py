def run_add_bold_tag(solution_class: type, s: str, words: list[str]):
    implementation = solution_class()
    return implementation.add_bold_tag(s, words)


def assert_add_bold_tag(result: str, expected: str) -> bool:
    assert result == expected
    return True
