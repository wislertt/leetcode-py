def run_max_product(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.max_product(words)


def assert_max_product(result: int, expected: int) -> bool:
    assert result == expected
    return True
