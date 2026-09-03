def run_word_filter(solution_class: type, operations: list[str], inputs: list[list[str]]):
    word_filter = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "WordFilter":
            word_filter = solution_class(words=inputs[i][0])
            results.append(None)
        elif op == "f" and word_filter is not None:
            results.append(word_filter.f(pref=inputs[i][0], suff=inputs[i][1]))
    return results, word_filter


def assert_word_filter(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
