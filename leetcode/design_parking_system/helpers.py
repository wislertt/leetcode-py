def run_parking_system(solution_class: type, operations: list[str], inputs: list[list[int]]):
    system = None
    results: list[bool | None] = []
    for i, op in enumerate(operations):
        if op == "ParkingSystem":
            system = solution_class(inputs[i][0], inputs[i][1], inputs[i][2])
            results.append(None)
        elif op == "add_car" and system is not None:
            results.append(system.add_car(inputs[i][0]))
    return results, system


def assert_parking_system(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
