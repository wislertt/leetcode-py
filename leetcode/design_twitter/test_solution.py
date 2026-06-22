from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_twitter, run_twitter
from .solution import Twitter


class TestDesignTwitter:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "Twitter",
                    "postTweet",
                    "getNewsFeed",
                    "follow",
                    "postTweet",
                    "getNewsFeed",
                    "unfollow",
                    "getNewsFeed",
                ],
                [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
                [None, None, [5], None, None, [6, 5], None, [5]],
            ),
            (
                ["Twitter", "postTweet", "postTweet", "postTweet", "getNewsFeed"],
                [[], [1, 1], [1, 2], [1, 3], [1]],
                [None, None, None, None, [3, 2, 1]],
            ),
            (
                ["Twitter", "postTweet", "postTweet", "follow", "getNewsFeed"],
                [[], [1, 10], [2, 20], [1, 2], [1]],
                [None, None, None, None, [20, 10]],
            ),
            (
                ["Twitter", "follow", "follow", "postTweet", "postTweet", "getNewsFeed"],
                [[], [1, 2], [1, 3], [2, 100], [3, 200], [1]],
                [None, None, None, None, None, [200, 100]],
            ),
            (
                ["Twitter", "postTweet", "follow", "getNewsFeed", "unfollow", "getNewsFeed"],
                [[], [2, 50], [1, 2], [1], [1, 2], [1]],
                [None, None, None, [50], None, []],
            ),
            (["Twitter", "postTweet", "getNewsFeed"], [[], [1, 5], [1]], [None, None, [5]]),
            (
                [
                    "Twitter",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "getNewsFeed",
                ],
                [
                    [],
                    [1, 1],
                    [1, 2],
                    [1, 3],
                    [1, 4],
                    [1, 5],
                    [1, 6],
                    [1, 7],
                    [1, 8],
                    [1, 9],
                    [1, 10],
                    [1, 11],
                    [1, 12],
                    [1],
                ],
                [
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3],
                ],
            ),
            (
                ["Twitter", "postTweet", "postTweet", "unfollow", "getNewsFeed"],
                [[], [1, 7], [1, 8], [1, 1], [1]],
                [None, None, None, None, [8, 7]],
            ),
            (
                [
                    "Twitter",
                    "follow",
                    "postTweet",
                    "postTweet",
                    "getNewsFeed",
                    "unfollow",
                    "getNewsFeed",
                ],
                [[], [1, 2], [2, 30], [1, 40], [1], [1, 2], [1]],
                [None, None, None, None, [40, 30], None, [40]],
            ),
            (
                [
                    "Twitter",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "postTweet",
                    "getNewsFeed",
                    "getNewsFeed",
                ],
                [[], [1, 11], [1, 22], [1, 33], [1, 44], [1, 55], [1], [1]],
                [None, None, None, None, None, None, [55, 44, 33, 22, 11], [55, 44, 33, 22, 11]],
            ),
            (
                ["Twitter", "follow", "postTweet", "getNewsFeed", "getNewsFeed"],
                [[], [1, 2], [2, 99], [1], [2]],
                [None, None, None, [99], [99]],
            ),
            (
                [
                    "Twitter",
                    "postTweet",
                    "postTweet",
                    "follow",
                    "follow",
                    "getNewsFeed",
                    "unfollow",
                    "getNewsFeed",
                ],
                [[], [1, 1], [2, 2], [1, 2], [1, 2], [1], [1, 2], [1]],
                [None, None, None, None, None, [2, 1], None, [1]],
            ),
            (
                ["Twitter", "follow", "postTweet", "postTweet", "postTweet", "getNewsFeed"],
                [[], [1, 2], [1, 1], [2, 2], [2, 3], [1]],
                [None, None, None, None, None, [3, 2, 1]],
            ),
        ],
    )
    def test_twitter(self, operations: list[str], inputs: list[list[int]], expected: list[Any]):
        result = run_twitter(Twitter, operations, inputs)
        assert_twitter(result, expected)
