import pytest

from leetcode_py import logged_test

from .helpers import assert_min_mutation, run_min_mutation
from .solution import Solution


class TestMinimumGeneticMutation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "start_gene, end_gene, bank, expected",
        [
            ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
            ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
            ("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3),
            ("AACCGGTT", "AACCGGTA", [], -1),
            ("AACCGGTT", "AACCGGTT", [], 0),
            ("AACCGGTT", "AACCGGTA", ["AACCGGTT"], -1),
            ("AACCGGTT", "AACCGGTT", ["AACCGGTA"], 0),
            ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AAACGGTA"], 2),
            ("AACCGGTT", "AACCGGTA", ["AACCGGTA", "AACCGGTT", "AACCGGTC"], 1),
            ("CTAATGGA", "CCTCGAAA", ["CTAAGGGA", "CTATTGGA"], -1),
            ("GCGCCTTT", "GCCTTAGG", ["GCGCCTTC"], -1),
            ("CGTGTAGG", "CCACTGGG", ["GGTGTAGG", "CTTGTAGG", "CGTGTTGG", "CGTGCAGG"], -1),
            ("AACAGACG", "CATCTACA", ["GACAGACG", "AACAGTCG", "AAAAGACG", "TACAGACG"], -1),
            ("AGGCTTGG", "TGAACGAC", ["AGGCTTTG", "AGGGTTGG", "AGGCTAGG"], -1),
            ("GGTGCGGA", "AGTGCGGA", ["AGTGCGGA"], 1),
            ("GTAGAACG", "GTAGAAAG", ["GTAGAAAG"], 1),
            ("TAACGTTA", "AGACGCTA", ["AAACGTTA", "AGACGTTA", "AGACGCTA"], 3),
        ],
    )
    def test_min_mutation(self, start_gene: str, end_gene: str, bank: list[str], expected: int):
        result = run_min_mutation(Solution, start_gene, end_gene, bank)
        assert_min_mutation(result, expected)
