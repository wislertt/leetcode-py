def run_autocomplete_system(solution_class: type, operations: list[str], inputs: list[list]):
    system = None
    results: list[list[str] | None] = []
    for i, op in enumerate(operations):
        if op == "AutocompleteSystem":
            system = solution_class(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "input" and system is not None:
            results.append(system.input(inputs[i][0]))
    return results, system


def assert_autocomplete_system(
    result: list[list[str] | None], expected: list[list[str] | None]
) -> bool:
    assert result == expected
    return True
