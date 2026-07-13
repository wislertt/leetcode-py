def run_hit_counter(solution_class: type, operations: list[str], inputs: list[list[int]]):
    counter = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "HitCounter":
            counter = solution_class()
            results.append(None)
        elif op == "hit" and counter is not None:
            counter.hit(inputs[i][0])
            results.append(None)
        elif op == "get_hits" and counter is not None:
            results.append(counter.get_hits(inputs[i][0]))
    return results, counter


def assert_hit_counter(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
