def run_num_buses_to_destination(
    solution_class: type, routes: list[list[int]], source: int, target: int
):
    implementation = solution_class()
    return implementation.num_buses_to_destination(routes, source, target)


def assert_num_buses_to_destination(result: int, expected: int) -> bool:
    assert result == expected
    return True
