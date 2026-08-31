def run_restore_ip_addresses(solution_class: type, s: str):
    implementation = solution_class()
    return sorted(implementation.restore_ip_addresses(s))


def assert_restore_ip_addresses(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
