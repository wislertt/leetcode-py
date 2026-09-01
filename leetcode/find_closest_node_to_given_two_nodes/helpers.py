def run_closest_meeting_node(solution_class: type, edges: list[int], node1: int, node2: int):
    implementation = solution_class()
    return implementation.closest_meeting_node(edges, node1, node2)


def assert_closest_meeting_node(result: int, expected: int) -> bool:
    assert result == expected
    return True
