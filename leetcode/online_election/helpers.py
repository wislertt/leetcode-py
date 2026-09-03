def run_online_election(solution_class: type, operations: list[str], inputs: list[list]):
    candidate = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "TopVotedCandidate":
            candidate = solution_class(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "q" and candidate is not None:
            results.append(candidate.q(inputs[i][0]))
    return results, candidate


def assert_online_election(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
