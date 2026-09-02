def run_most_profitable_path(
    solution_class: type, edges: list[list[int]], bob: int, amount: list[int]
):
    implementation = solution_class()
    return implementation.most_profitable_path(edges, bob, amount)


def assert_most_profitable_path(result: int, expected: int) -> bool:
    assert result == expected
    return True
