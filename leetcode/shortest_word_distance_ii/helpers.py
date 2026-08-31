def run_shortest_word_distance_ii(
    solution_class: type, operations: list[str], inputs: list[list[str]]
):
    distance = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "WordDistance":
            distance = solution_class(inputs[i])
            results.append(None)
        elif op == "shortest" and distance is not None:
            results.append(distance.shortest(inputs[i][0], inputs[i][1]))
    return results, distance


def assert_shortest_word_distance_ii(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
