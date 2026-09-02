def run_logger_rate_limiter(solution_class: type, operations: list[str], inputs: list[list]):
    logger = None
    results: list[bool | None] = []
    for i, op in enumerate(operations):
        if op == "Logger":
            logger = solution_class()
            results.append(None)
        elif op == "should_print_message" and logger is not None:
            results.append(logger.should_print_message(inputs[i][0], inputs[i][1]))
    return results, logger


def assert_logger_rate_limiter(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
