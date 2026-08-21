def run_my_queue(solution_class: type, operations: list[str], inputs: list[list[int]]):
    queue = None
    results: list[int | bool | None] = []
    for i, op in enumerate(operations):
        if op == "MyQueue":
            queue = solution_class()
            results.append(None)
        elif op == "push" and queue is not None:
            queue.push(inputs[i][0])
            results.append(None)
        elif op == "pop" and queue is not None:
            results.append(queue.pop())
        elif op == "peek" and queue is not None:
            results.append(queue.peek())
        elif op == "empty" and queue is not None:
            results.append(queue.empty())
    return results, queue


def assert_my_queue(result: list[int | bool | None], expected: list[int | bool | None]) -> bool:
    assert result == expected
    return True
