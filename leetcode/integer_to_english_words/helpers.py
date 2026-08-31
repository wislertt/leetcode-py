def run_number_to_words(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.number_to_words(num)


def assert_number_to_words(result: str, expected: str) -> bool:
    assert result == expected
    return True
