def run_generate_parenthesis(solution_class: type, n: int):
    implementation = solution_class()
    return sorted(implementation.generate_parenthesis(n))


def assert_generate_parenthesis(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
