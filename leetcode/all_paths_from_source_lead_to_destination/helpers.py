def run_leads_to_destination(
    solution_class: type, n: int, edges: list[list[int]], source: int, destination: int
):
    implementation = solution_class()
    return implementation.leads_to_destination(n, edges, source, destination)


def assert_leads_to_destination(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
