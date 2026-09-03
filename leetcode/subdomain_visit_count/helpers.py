def run_subdomain_visits(solution_class: type, cpdomains: list[str]):
    implementation = solution_class()
    return implementation.subdomain_visits(cpdomains)


def assert_subdomain_visits(result: list[str], expected: list[str]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    assert sorted(result) == sorted(expected)
    return True
