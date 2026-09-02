def run_ip_to_cidr(solution_class: type, ip: str, n: int):
    implementation = solution_class()
    return implementation.ip_to_cidr(ip, n)


def assert_ip_to_cidr(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
