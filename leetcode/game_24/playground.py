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
from helpers import assert_judge_point24, run_judge_point24
from solution import Solution

# %%
# Example test case
cards = [4, 1, 8, 7]
expected = True

# %%
result = run_judge_point24(Solution, cards)
result

# %%
assert_judge_point24(result, expected)
