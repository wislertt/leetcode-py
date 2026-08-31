def run_shortest_way(solution_class: type, source: str, target: str):
    implementation = solution_class()
    return implementation.shortest_way(source, target)


def assert_shortest_way(result: int, expected: int) -> bool:
    assert result == expected
    return True
