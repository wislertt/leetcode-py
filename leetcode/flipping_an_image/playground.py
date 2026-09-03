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
from helpers import assert_flip_and_invert_image, run_flip_and_invert_image
from solution import Solution

# %%
# Example test case
image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

# %%
result = run_flip_and_invert_image(Solution, image)
result

# %%
assert_flip_and_invert_image(result, expected)
