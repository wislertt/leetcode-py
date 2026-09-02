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
from helpers import assert_is_valid, run_is_valid
from solution import Solution

# %%
# Example test case
code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
expected = True

# %%
result = run_is_valid(Solution, code)
result

# %%
assert_is_valid(result, expected)
