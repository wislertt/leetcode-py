# Encode and Decode TinyURL

**Difficulty:** Medium
**Topics:** Hash Table, String, Design
**Tags:** neetcode

**LeetCode:** [Problem 535](https://leetcode.com/problems/encode-and-decode-tinyurl/description/)

## Problem Description

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`. Design a class to encode a URL and decode a tiny URL.

> Note: This is a companion problem to the System Design problem: Design TinyURL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the `Codec` class:

- `Codec()` Initializes the object of the system.
- `String encode(String longUrl)` Returns a tiny URL for the given `longUrl`.
- `String decode(String shortUrl)` Returns the original long URL for the given `shortUrl`. It is guaranteed that the given `shortUrl` was encoded by the same object.

## Examples

### Example 1:

```
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Codec codec = new Codec();
string tiny = codec.encode(url); // returns the encoded tiny url.
string ans = codec.decode(tiny); // returns the original url after decoding it.
```

## Constraints

- `1 <= url.length <= 10^4`
- `url` is guranteed to be a valid URL.
