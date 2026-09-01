def run_seat_reservation_manager(
    solution_class: type, operations: list[str], inputs: list[list[int]]
):
    manager = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "SeatManager":
            manager = solution_class(inputs[i][0])
            results.append(None)
        elif op == "reserve" and manager is not None:
            results.append(manager.reserve())
        elif op == "unreserve" and manager is not None:
            manager.unreserve(inputs[i][0])
            results.append(None)
    return results, manager


def assert_seat_reservation_manager(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
