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
from helpers import assert_generate_sentences, run_generate_sentences
from solution import Solution

# %%
# Example test case
synonyms = [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]
text = "happy sad"
expected = [
    "cheerful sad",
    "cheerful sorrow",
    "happy sad",
    "happy sorrow",
    "joy sad",
    "joy sorrow",
]

# %%
result = run_generate_sentences(Solution, synonyms, text)
result

# %%
assert_generate_sentences(result, expected)
