def run_underground_system_operations(
    solution_class: type, operations: list[str], inputs: list[list]
):
    system = None
    results: list[float | None] = []
    for i, op in enumerate(operations):
        if op == "UndergroundSystem":
            system = solution_class()
            results.append(None)
        elif op == "check_in" and system is not None:
            system.check_in(*inputs[i])
            results.append(None)
        elif op == "check_out" and system is not None:
            system.check_out(*inputs[i])
            results.append(None)
        elif op == "get_average_time" and system is not None:
            results.append(system.get_average_time(inputs[i][0], inputs[i][1]))
    return results, system


def assert_underground_system_operations(
    result: list[float | None], expected: list[float | None]
) -> bool:
    assert len(result) == len(expected)
    for got, want in zip(result, expected, strict=True):
        if got is None or want is None:
            assert got == want
        else:
            assert abs(got - want) <= 1e-5
    return True
