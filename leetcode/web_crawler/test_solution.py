import pytest

from leetcode_py import logged_test

from .helpers import assert_crawl, run_crawl
from .solution import Solution


class TestWebCrawler:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "urls, edges, start_url, expected",
        [
            (
                [
                    "http://news.yahoo.com",
                    "http://news.yahoo.com/news",
                    "http://news.yahoo.com/news/topics/",
                    "http://news.google.com",
                    "http://news.yahoo.com/us",
                ],
                [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]],
                "http://news.yahoo.com/news/topics/",
                [
                    "http://news.yahoo.com",
                    "http://news.yahoo.com/news",
                    "http://news.yahoo.com/news/topics/",
                    "http://news.yahoo.com/us",
                ],
            ),
            (
                [
                    "http://news.yahoo.com",
                    "http://news.yahoo.com/news",
                    "http://news.yahoo.com/news/topics/",
                    "http://news.google.com",
                ],
                [[0, 2], [2, 1], [3, 2], [3, 1], [3, 0]],
                "http://news.google.com",
                ["http://news.google.com"],
            ),
            (["http://a.com"], [], "http://a.com", ["http://a.com"]),
            (
                ["http://a.com", "http://a.com/b", "http://a.com/b/c"],
                [[0, 1], [1, 2]],
                "http://a.com",
                ["http://a.com", "http://a.com/b", "http://a.com/b/c"],
            ),
            (
                ["http://a.com", "http://b.com", "http://a.com/c"],
                [[0, 1], [1, 2]],
                "http://a.com",
                ["http://a.com"],
            ),
            (
                ["http://a.com", "http://b.com", "http://a.com/x"],
                [[0, 1], [1, 2]],
                "http://b.com",
                ["http://b.com"],
            ),
            (
                ["http://a.com", "http://a.com.evil.com", "http://a.com/x"],
                [[0, 1], [1, 2], [0, 2]],
                "http://a.com",
                ["http://a.com", "http://a.com/x"],
            ),
            (
                ["http://a.com", "http://a.com/", "http://a.com/home"],
                [[0, 1], [1, 2]],
                "http://a.com",
                ["http://a.com", "http://a.com/", "http://a.com/home"],
            ),
            (
                ["http://a.com/1", "http://a.com/2", "http://a.com/3"],
                [[0, 1], [1, 2], [2, 0]],
                "http://a.com/1",
                ["http://a.com/1", "http://a.com/2", "http://a.com/3"],
            ),
            (
                ["http://a.com", "http://a.com/z"],
                [[0, 0], [0, 1]],
                "http://a.com",
                ["http://a.com", "http://a.com/z"],
            ),
            (
                ["http://a.com", "http://a.com/dup", "http://a.com/other"],
                [[0, 1], [0, 1], [0, 2]],
                "http://a.com",
                ["http://a.com", "http://a.com/dup", "http://a.com/other"],
            ),
            (
                ["http://a.com", "http://a.com/1", "http://a.com/2"],
                [[1, 2]],
                "http://a.com",
                ["http://a.com"],
            ),
            (
                ["http://a.com/1", "http://a.com", "http://a.com/2"],
                [[0, 1], [1, 2]],
                "http://a.com",
                ["http://a.com", "http://a.com/2"],
            ),
            (
                [
                    "http://a.com/1",
                    "http://a.com/2",
                    "http://b.com/1",
                    "http://a.com/3",
                    "http://a.com/4",
                ],
                [[0, 1], [1, 2], [2, 3], [3, 4]],
                "http://a.com/1",
                ["http://a.com/1", "http://a.com/2"],
            ),
            (
                [
                    "http://c.net",
                    "http://b.org/x1",
                    "http://c.net/p2",
                    "http://news.a.com",
                    "http://c.net/x4",
                    "http://c.net/p6",
                ],
                [[0, 3]],
                "http://c.net/p2",
                ["http://c.net/p2"],
            ),
            (
                [
                    "http://a.com/p0",
                    "http://b.org/us1",
                    "http://b.org",
                    "http://a.com/us3",
                    "http://b.org/topics4",
                    "http://b.org/p5",
                ],
                [
                    [2, 5],
                    [5, 1],
                    [4, 5],
                    [3, 0],
                    [4, 2],
                    [4, 5],
                    [0, 3],
                    [5, 0],
                    [3, 4],
                    [1, 5],
                    [2, 0],
                ],
                "http://b.org/p5",
                ["http://b.org/p5", "http://b.org/us1"],
            ),
            (
                [
                    "http://b.org",
                    "http://c.net/topics1",
                    "http://a.com/topics2",
                    "http://c.net/news3",
                    "http://b.org/x5",
                ],
                [[0, 1], [4, 3], [4, 2], [1, 1], [1, 3]],
                "http://b.org/x5",
                ["http://b.org/x5"],
            ),
            (
                [
                    "http://b.org",
                    "http://a.com/topics1",
                    "http://news.a.com",
                    "http://b.org/us5",
                    "http://a.com",
                    "http://news.a.com/x7",
                ],
                [[2, 0], [0, 5], [1, 0], [1, 3], [0, 5], [2, 1], [3, 2], [0, 5], [0, 4]],
                "http://b.org",
                ["http://b.org"],
            ),
        ],
    )
    def test_crawl(
        self, urls: list[str], edges: list[list[int]], start_url: str, expected: list[str]
    ):
        result = run_crawl(Solution, urls, edges, start_url)
        assert_crawl(result, expected)
