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
from helpers import assert_num_k_len_substr_no_repeats, run_num_k_len_substr_no_repeats
from solution import Solution

# %%
# Example test case
s = "havefunonleetcode"
k = 5
expected = 6

# %%
result = run_num_k_len_substr_no_repeats(Solution, s, k)
result

# %%
assert_num_k_len_substr_no_repeats(result, expected)
