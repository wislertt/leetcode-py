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
from helpers import assert_uncommon_from_sentences, run_uncommon_from_sentences
from solution import Solution

# %%
# Example test case
s1 = "this apple is sweet"
s2 = "this apple is sour"
expected = ["sweet", "sour"]

# %%
result = run_uncommon_from_sentences(Solution, s1, s2)
result

# %%
assert_uncommon_from_sentences(result, expected)
