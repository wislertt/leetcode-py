def run_valid_ip_address(solution_class: type, query_ip: str):
    implementation = solution_class()
    return implementation.valid_ip_address(query_ip)


def assert_valid_ip_address(result: str, expected: str) -> bool:
    assert result == expected
    return True
