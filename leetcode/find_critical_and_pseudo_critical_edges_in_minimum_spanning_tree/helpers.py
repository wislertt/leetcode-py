def run_find_critical_and_pseudo_critical_edges(
    solution_class: type, n: int, edges: list[list[int]]
):
    implementation = solution_class()
    return implementation.find_critical_and_pseudo_critical_edges(n, edges)


def assert_find_critical_and_pseudo_critical_edges(
    result: list[list[int]], expected: list[list[int]]
) -> bool:
    critical, pseudo = result
    exp_critical, exp_pseudo = expected
    # Edge order within each list is unspecified; compare as sorted sets.
    assert sorted(critical) == sorted(exp_critical)
    assert sorted(pseudo) == sorted(exp_pseudo)
    return True
