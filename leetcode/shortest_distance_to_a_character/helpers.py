def run_shortest_to_char(solution_class: type, s: str, c: str):
    implementation = solution_class()
    return implementation.shortest_to_char(s, c)


def assert_shortest_to_char(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
