from typing import Any


def run_online_stock_span_operations(
    solution_class: type, operations: list[str], inputs: list[list[int]]
):
    spanner: Any = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "StockSpanner":
            spanner = solution_class()
            results.append(None)
        elif op == "next" and spanner is not None:
            results.append(spanner.next(inputs[i][0]))
    return results


def assert_online_stock_span_operations(
    result: list[int | None], expected: list[int | None]
) -> bool:
    assert result == expected
    return True
