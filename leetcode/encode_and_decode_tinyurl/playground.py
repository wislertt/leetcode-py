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
from helpers import assert_encode_and_decode_tinyurl, run_encode_and_decode_tinyurl
from solution import Codec

# %%
# Example test case
operations = ["Codec", "encode", "decode"]
inputs = [[""], ["https://leetcode.com/problems/design-tinyurl"], []]
expected = [None, None, "https://leetcode.com/problems/design-tinyurl"]

# %%
result, codec = run_encode_and_decode_tinyurl(Codec, operations, inputs)
print(result)
codec

# %%
assert_encode_and_decode_tinyurl(result, expected)
