def run_min_mutation(solution_class: type, start_gene: str, end_gene: str, bank: list[str]):
    implementation = solution_class()
    return implementation.min_mutation(start_gene, end_gene, bank)


def assert_min_mutation(result: int, expected: int) -> bool:
    assert result == expected
    return True
