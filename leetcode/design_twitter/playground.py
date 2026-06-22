# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_twitter, run_twitter
from solution import Twitter

# %%
# Example test case
operations = [
    "Twitter",
    "postTweet",
    "getNewsFeed",
    "follow",
    "postTweet",
    "getNewsFeed",
    "unfollow",
    "getNewsFeed",
]
inputs = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
expected = [None, None, [5], None, None, [6, 5], None, [5]]

# %%
result = run_twitter(Twitter, operations, inputs)
result

# %%
assert_twitter(result, expected)
