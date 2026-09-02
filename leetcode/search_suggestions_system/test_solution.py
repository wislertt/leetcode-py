import pytest

from leetcode_py import logged_test

from .helpers import assert_suggested_products, run_suggested_products
from .solution import Solution


class TestSearchSuggestionsSystem:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "products, search_word, expected",
        [
            [
                ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
                "mouse",
                [
                    ["mobile", "moneypot", "monitor"],
                    ["mobile", "moneypot", "monitor"],
                    ["mouse", "mousepad"],
                    ["mouse", "mousepad"],
                    ["mouse", "mousepad"],
                ],
            ],
            [
                ["havana"],
                "havana",
                [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
            ],
            [
                ["bags", "bagend", "baggage", "bagger", "baguette"],
                "bags",
                [
                    ["bagend", "baggage", "bagger"],
                    ["bagend", "baggage", "bagger"],
                    ["bagend", "baggage", "bagger"],
                    ["bags"],
                ],
            ],
            [["abc"], "abcd", [["abc"], ["abc"], ["abc"], []]],
            [["a"], "a", [["a"]]],
            [
                ["apple", "app", "application"],
                "app",
                [
                    ["app", "apple", "application"],
                    ["app", "apple", "application"],
                    ["app", "apple", "application"],
                ],
            ],
            [["zebra", "zip", "zoo"], "z", [["zebra", "zip", "zoo"]]],
            [
                ["cat", "cattle", "caterpillar"],
                "catx",
                [
                    ["cat", "caterpillar", "cattle"],
                    ["cat", "caterpillar", "cattle"],
                    ["cat", "caterpillar", "cattle"],
                    [],
                ],
            ],
            [["p"], "p", [["p"]]],
            [
                ["data", "date", "database", "datetime"],
                "dat",
                [
                    ["data", "database", "date"],
                    ["data", "database", "date"],
                    ["data", "database", "date"],
                ],
            ],
            [["a", "aabab"], "ba", [[], []]],
            [["abbb", "a", "aab", "b"], "bab", [["b"], [], []]],
            [["abab", "a", "bb", "b", "ab"], "aaaa", [["a", "ab", "abab"], [], [], []]],
            [
                ["bbab", "babaa", "baaab", "baba", "abb", "aabaa", "ababb"],
                "babb",
                [["baaab", "baba", "babaa"], ["baaab", "baba", "babaa"], ["baba", "babaa"], []],
            ],
            [
                ["ba", "a", "aaaa", "abaaa", "b", "ab", "bbbbb"],
                "bb",
                [["b", "ba", "bbbbb"], ["bbbbb"]],
            ],
            [["a", "b", "bb"], "ab", [["a"], []]],
        ],
    )
    def test_suggested_products(
        self, products: list[str], search_word: str, expected: list[list[str]]
    ):
        result = run_suggested_products(Solution, products, search_word)
        assert_suggested_products(result, expected)
