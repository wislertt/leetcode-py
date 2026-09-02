# Count Vowel Strings in Ranges

**Difficulty:** Medium
**Topics:** Array, String, Prefix Sum
**Tags:** neetcode

**LeetCode:** [Problem 2559](https://leetcode.com/problems/count-vowel-strings-in-ranges/description/)

## Problem Description

You are given a <strong>0-indexed</strong> array of strings <code>words</code> and a 2D array of integers <code>queries</code>.

Each query <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> asks us to find the number of strings present at the indices ranging from <code>l<sub>i</sub></code> to <code>r<sub>i</sub></code> (both <strong>inclusive</strong>) of <code>words</code> that start and end with a vowel.

Return <em>an array </em><code>ans</code><em> of size </em><code>queries.length</code><em>, where </em><code>ans[i]</code><em> is the answer to the </em><code>i</code><sup>th</sup><em> query</em>.

<strong>Note</strong> that the vowel letters are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>.

## Examples

### Example 1:

```
Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
The answer to the query [1,4] is 3 (strings "ece", "aa", "e").
The answer to the query [1,1] is 0.
We return [2,3,0].
```

### Example 2:

```
Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
```

## Constraints

- 1 <= words.length <= 10^5
- 1 <= words[i].length <= 40
- words[i] consists only of lowercase English letters.
- sum(words[i].length) <= 3 * 10^5
- 1 <= queries.length <= 10^5
- 0 <= l<sub>i</sub> <= r<sub>i</sub> < words.length
