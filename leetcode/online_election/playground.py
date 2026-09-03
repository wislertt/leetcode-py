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
from helpers import assert_online_election, run_online_election
from solution import TopVotedCandidate

# %%
# Example test case
operations = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
inputs = [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
expected = [None, 0, 1, 1, 0, 0, 1]

# %%
result, candidate = run_online_election(TopVotedCandidate, operations, inputs)
print(result)
candidate

# %%
assert_online_election(result, expected)
