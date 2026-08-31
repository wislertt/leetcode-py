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
from helpers import assert_count_of_atoms, run_count_of_atoms
from solution import Solution

# %%
# Example test case
formula = "H2O"
expected = "H2O"

# %%
result = run_count_of_atoms(Solution, formula)
result

# %%
assert_count_of_atoms(result, expected)
