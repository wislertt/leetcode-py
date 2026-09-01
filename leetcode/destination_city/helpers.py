def run_dest_city(solution_class: type, paths: list[list[str]]):
    implementation = solution_class()
    return implementation.dest_city(paths)


def assert_dest_city(result: str, expected: str) -> bool:
    assert result == expected
    return True
