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
from helpers import assert_suggested_products, run_suggested_products
from solution import Solution

# %%
# Example test case
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
search_word = "mouse"
expected = [
    ["mobile", "moneypot", "monitor"],
    ["mobile", "moneypot", "monitor"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"],
]

# %%
result = run_suggested_products(Solution, products, search_word)
result

# %%
assert_suggested_products(result, expected)
