def run_browser_history_operations(solution_class: type, operations: list[str], inputs: list[list]):
    history = None
    results: list[str | None] = []
    for i, op in enumerate(operations):
        if op == "BrowserHistory":
            history = solution_class(inputs[i][0])
            results.append(None)
        elif op == "visit" and history is not None:
            history.visit(inputs[i][0])
            results.append(None)
        elif op == "back" and history is not None:
            results.append(history.back(inputs[i][0]))
        elif op == "forward" and history is not None:
            results.append(history.forward(inputs[i][0]))
    return results, history


def assert_browser_history_operations(result: list[str | None], expected: list[str | None]) -> bool:
    assert result == expected
    return True
