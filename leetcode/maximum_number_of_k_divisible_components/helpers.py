def run_max_k_divisible_components(
    solution_class: type, n: int, edges: list[list[int]], values: list[int], k: int
):
    implementation = solution_class()
    return implementation.max_k_divisible_components(n, edges, values, k)


def assert_max_k_divisible_components(result: int, expected: int) -> bool:
    assert result == expected
    return True
