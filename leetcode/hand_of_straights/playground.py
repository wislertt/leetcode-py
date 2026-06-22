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
from helpers import assert_is_n_straight_hand, run_is_n_straight_hand
from solution import Solution

# %%
# Example test case
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
group_size = 3
expected = True

# %%
result = run_is_n_straight_hand(Solution, hand, group_size)
result

# %%
assert_is_n_straight_hand(result, expected)
