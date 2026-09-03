def run_circular_deque(solution_class: type, operations: list[str], inputs: list[list[int]]):
    deq = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "MyCircularDeque":
            deq = solution_class(inputs[i][0])
            results.append(None)
        elif op == "insert_front" and deq is not None:
            results.append(deq.insert_front(inputs[i][0]))
        elif op == "insert_last" and deq is not None:
            results.append(deq.insert_last(inputs[i][0]))
        elif op == "delete_front" and deq is not None:
            results.append(deq.delete_front())
        elif op == "delete_last" and deq is not None:
            results.append(deq.delete_last())
        elif op == "get_front" and deq is not None:
            results.append(deq.get_front())
        elif op == "get_rear" and deq is not None:
            results.append(deq.get_rear())
        elif op == "is_empty" and deq is not None:
            results.append(deq.is_empty())
        elif op == "is_full" and deq is not None:
            results.append(deq.is_full())
    return results, deq


def assert_circular_deque(
    result: list[int | bool | None], expected: list[int | bool | None]
) -> bool:
    assert result == expected
    return True
