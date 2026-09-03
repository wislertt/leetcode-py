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
from helpers import assert_remove_comments, run_remove_comments
from solution import Solution

# %%
# Example test case
source = ["a/*comment", "line", "more_comment*/b"]
expected = ["ab"]

# %%
result = run_remove_comments(Solution, source, expected)
result

# %%
assert_remove_comments(result, expected)
