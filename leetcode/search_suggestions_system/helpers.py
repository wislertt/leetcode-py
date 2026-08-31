def run_suggested_products(solution_class: type, products: list[str], search_word: str):
    implementation = solution_class()
    return implementation.suggested_products(products, search_word)


def assert_suggested_products(result: list[list[str]], expected: list[list[str]]) -> bool:
    assert result == expected
    return True
