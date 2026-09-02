def run_valid_word_abbr(solution_class: type, operations: list[str], inputs: list[list[str]]):
    implementation = None
    results: list[bool | None] = []
    for i, op in enumerate(operations):
        if op == "ValidWordAbbr":
            implementation = solution_class(inputs[i])
            results.append(None)
        elif op == "is_unique" and implementation is not None:
            results.append(implementation.is_unique(inputs[i][0]))
    return results, implementation


def assert_valid_word_abbr(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
