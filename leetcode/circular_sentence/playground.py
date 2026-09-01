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
from helpers import assert_is_circular_sentence, run_is_circular_sentence
from solution import Solution

# %%
# Example test case
sentence = "leetcode exercises sound delightful"
expected = True

# %%
result = run_is_circular_sentence(Solution, sentence)
result

# %%
assert_is_circular_sentence(result, expected)
