# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_crawl, run_crawl
from solution import Solution

# %%
# Example test case
urls = [
    "http://news.yahoo.com",
    "http://news.yahoo.com/news",
    "http://news.yahoo.com/news/topics/",
    "http://news.google.com",
    "http://news.yahoo.com/us",
]
edges = [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]
start_url = "http://news.yahoo.com/news/topics/"
expected = sorted(
    [
        "http://news.yahoo.com",
        "http://news.yahoo.com/news",
        "http://news.yahoo.com/news/topics/",
        "http://news.yahoo.com/us",
    ]
)

# %%
result = run_crawl(Solution, urls, edges, start_url)
result

# %%
assert_crawl(result, expected)
