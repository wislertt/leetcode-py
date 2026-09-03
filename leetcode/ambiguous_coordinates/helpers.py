def run_ambiguous_coordinates(solution_class: type, s: str):
    implementation = solution_class()
    return sorted(implementation.ambiguous_coordinates(s))


def assert_ambiguous_coordinates(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
