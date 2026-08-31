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
from helpers import assert_max_number_of_balloons, run_max_number_of_balloons
from solution import Solution

# %%
# Example test case
text = "loonbalxballpoon"
expected = 2

# %%
result = run_max_number_of_balloons(Solution, text)
result

# %%
assert_max_number_of_balloons(result, expected)
