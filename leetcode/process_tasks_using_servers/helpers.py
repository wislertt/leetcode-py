def run_assign_tasks(solution_class: type, servers: list[int], tasks: list[int]):
    implementation = solution_class()
    return implementation.assign_tasks(servers, tasks)


def assert_assign_tasks(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
