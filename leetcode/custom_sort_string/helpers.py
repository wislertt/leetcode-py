def run_custom_sort_string(solution_class: type, order: str, s: str):
    implementation = solution_class()
    return implementation.custom_sort_string(order, s)


def assert_custom_sort_string(result: str, expected: str) -> bool:
    # Multiple valid answers exist; the solution is a deterministic stable
    # rank sort, so its canonical output is compared for exact equality
    assert result == expected
    return True
