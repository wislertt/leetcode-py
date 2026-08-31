from typing import Any


def run_data_stream_as_disjoint_intervals(
    solution_class: type, operations: list[str], inputs: list[list[Any]]
):
    summary: Any = None
    results: list[Any] = []

    for op, args in zip(operations, inputs, strict=False):
        if op == "SummaryRanges":
            summary = solution_class()
            results.append(None)
        elif op == "addNum":
            assert summary is not None
            summary.add_num(args[0])
            results.append(None)
        elif op == "getIntervals":
            assert summary is not None
            results.append(summary.get_intervals())

    return results


def assert_data_stream_as_disjoint_intervals(result: list[Any], expected: list[Any]) -> bool:
    assert result == expected
    return True
