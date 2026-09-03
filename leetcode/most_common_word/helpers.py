def run_most_common_word(solution_class: type, paragraph: str, banned: list[str]):
    implementation = solution_class()
    return implementation.most_common_word(paragraph, banned)


def assert_most_common_word(result: str, expected: str) -> bool:
    assert result == expected
    return True
