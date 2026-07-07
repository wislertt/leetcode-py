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
from helpers import assert_longest_common_prefix, run_longest_common_prefix
from solution import Solution

# %%
# Example test case
strs = ["flower", "flow", "flight"]
expected = "fl"

# %%
result = run_longest_common_prefix(Solution, strs)
result

# %%
assert_longest_common_prefix(result, expected)
