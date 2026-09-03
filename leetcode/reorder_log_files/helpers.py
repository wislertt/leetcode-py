def run_reorder_log_files(solution_class: type, logs: list[str]):
    implementation = solution_class()
    return implementation.reorder_log_files(logs)


def assert_reorder_log_files(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
