def run_max_probability(
    solution_class: type,
    n: int,
    edges: list[list[int]],
    succ_prob: list[float],
    start_node: int,
    end_node: int,
):
    implementation = solution_class()
    return implementation.max_probability(n, edges, succ_prob, start_node, end_node)


def assert_max_probability(result: float, expected: float) -> bool:
    # The statement accepts answers within 10^-5 of the actual answer
    assert abs(result - expected) < 1e-5
    return True
