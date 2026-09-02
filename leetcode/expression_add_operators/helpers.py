def run_add_operators(solution_class: type, num: str, target: int):
    implementation = solution_class()
    return implementation.add_operators(num, target)


def assert_add_operators(result: list[str], expected: list[str]) -> bool:
    # Expression order is not significant, compare as multisets
    assert sorted(result) == sorted(expected)
    return True
