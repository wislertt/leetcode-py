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
from helpers import assert_add_bold_tag, run_add_bold_tag
from solution import Solution

# %%
# Example test case
s = "abcxyz123"
words = ["abc", "123"]
expected = "<b>abc</b>xyz<b>123</b>"

# %%
result = run_add_bold_tag(Solution, s, words)
result

# %%
assert_add_bold_tag(result, expected)
