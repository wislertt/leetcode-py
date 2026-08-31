import pytest

from leetcode_py import logged_test

from .helpers import assert_repeated_dna_sequences, run_repeated_dna_sequences
from .solution import Solution


class TestRepeatedDNASequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]),
            ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
            ("A", []),
            ("AAAAAAAAAA", []),
            ("AAAAAAAAAAA", ["AAAAAAAAAA"]),
            ("ACGTACGTAC", []),
            ("ACGTACGTACGTA", []),
            ("AAAAAGGGGGAAAAAGGGGG", ["AAAAAGGGGG"]),
            ("CCCCCCCCCCC", ["CCCCCCCCCC"]),
            ("ACACACACACACACACACAC", ["ACACACACAC", "CACACACACA"]),
            ("GGGGGGGGGGGGGG", ["GGGGGGGGGG"]),
            ("AAGTCCGTTAAGTCCGTT", []),
            ("TTTTTTTTTTTTTTTTTTTT", ["TTTTTTTTTT"]),
            ("CATGGCATGGCATGG", ["CATGGCATGG"]),
            (
                "GATTACAGATTACAGATTACA",
                ["ACAGATTACA", "ATTACAGATT", "GATTACAGAT", "TACAGATTAC", "TTACAGATTA"],
            ),
            ("ACGTACGTACGTACGTACGT", ["ACGTACGTAC", "CGTACGTACG", "GTACGTACGT", "TACGTACGTA"]),
            ("TAAAAATTTTTAAAAATTTTT", ["AAAAATTTTT", "TAAAAATTTT"]),
        ],
    )
    def test_repeated_dna_sequences(self, s: str, expected: list[str]):
        result = run_repeated_dna_sequences(Solution, s)
        assert_repeated_dna_sequences(result, expected)
