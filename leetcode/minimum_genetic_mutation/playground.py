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
from helpers import assert_min_mutation, run_min_mutation
from solution import Solution

# %%
# Example test case
start_gene = "AACCGGTT"
end_gene = "AACCGGTA"
bank = ["AACCGGTA"]
expected = 1

# %%
result = run_min_mutation(Solution, start_gene, end_gene, bank)
result

# %%
assert_min_mutation(result, expected)
