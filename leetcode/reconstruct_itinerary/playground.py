# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_find_itinerary, run_find_itinerary
from solution import Solution

# %%
# Example test case
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]

# %%
result = run_find_itinerary(Solution, tickets)
result

# %%
assert_find_itinerary(result, expected)
