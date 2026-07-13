# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_min_extra_char, run_min_extra_char
from solution import Solution

# %%
# Example test case
s = "leetscode"
dictionary = ["leet", "code", "leetcode"]
expected = 1

# %%
result = run_min_extra_char(Solution, s, dictionary)
result

# %%
assert_min_extra_char(result, expected)
