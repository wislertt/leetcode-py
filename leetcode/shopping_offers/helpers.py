def run_shopping_offers(
    solution_class: type, price: list[int], special: list[list[int]], needs: list[int]
):
    implementation = solution_class()
    return implementation.shopping_offers(price, special, needs)


def assert_shopping_offers(result: int, expected: int) -> bool:
    assert result == expected
    return True
