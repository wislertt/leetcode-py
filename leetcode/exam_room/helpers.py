def run_exam_room(solution_class: type, operations: list[str], inputs: list[list[int]]):
    room = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "ExamRoom":
            room = solution_class(inputs[i][0])
            results.append(None)
        elif op == "seat" and room is not None:
            results.append(room.seat())
        elif op == "leave" and room is not None:
            room.leave(inputs[i][0])
            results.append(None)
    return results, room


def assert_exam_room(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
