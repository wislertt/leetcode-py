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
from helpers import assert_repeated_dna_sequences, run_repeated_dna_sequences
from solution import Solution

# %%
# Example test case
s: str = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
expected: list[str] = ["AAAAACCCCC", "CCCCCAAAAA"]

# %%
result = run_repeated_dna_sequences(Solution, s)
result

# %%
assert_repeated_dna_sequences(result, expected)
