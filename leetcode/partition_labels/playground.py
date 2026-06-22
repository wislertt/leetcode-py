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
from helpers import assert_partition_labels, run_partition_labels
from solution import Solution

# %%
# Example test case
s = "ababcbacadefegdehijhklij"
expected = [9, 7, 8]

# %%
result = run_partition_labels(Solution, s)
result

# %%
assert_partition_labels(result, expected)
