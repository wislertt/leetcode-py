def run_minimum_cost(
    solution_class: type,
    source: str,
    target: str,
    original: list[str],
    changed: list[str],
    cost: list[int],
):
    implementation = solution_class()
    return implementation.minimum_cost(source, target, original, changed, cost)


def assert_minimum_cost(result: int, expected: int) -> bool:
    assert result == expected
    return True
