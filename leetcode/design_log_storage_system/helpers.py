def run_log_storage(solution_class: type, operations: list[str], inputs: list[list]):
    log_system = None
    results: list[list[int] | None] = []
    for i, op in enumerate(operations):
        if op == "LogSystem":
            log_system = solution_class()
            results.append(None)
        elif op == "put" and log_system is not None:
            log_system.put(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "retrieve" and log_system is not None:
            results.append(log_system.retrieve(inputs[i][0], inputs[i][1], inputs[i][2]))
    return results, log_system


def assert_log_storage(result: list[list[int] | None], expected: list[list[int] | None]) -> bool:
    # Order-independent comparison for retrieve results
    result_sorted = [sorted(r) if isinstance(r, list) else r for r in result]
    expected_sorted = [sorted(r) if isinstance(r, list) else r for r in expected]
    assert result_sorted == expected_sorted
    return True
