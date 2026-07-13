def run_circular_queue(solution_class: type, operations: list[str], inputs: list[list[int]]):
    queue = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "MyCircularQueue":
            queue = solution_class(inputs[i][0])
            results.append(None)
        elif op == "en_queue" and queue is not None:
            results.append(queue.en_queue(inputs[i][0]))
        elif op == "de_queue" and queue is not None:
            results.append(queue.de_queue())
        elif op == "front" and queue is not None:
            results.append(queue.front())
        elif op == "rear" and queue is not None:
            results.append(queue.rear())
        elif op == "is_empty" and queue is not None:
            results.append(queue.is_empty())
        elif op == "is_full" and queue is not None:
            results.append(queue.is_full())
    return results, queue


def assert_circular_queue(
    result: list[int | bool | None], expected: list[int | bool | None]
) -> bool:
    assert result == expected
    return True
