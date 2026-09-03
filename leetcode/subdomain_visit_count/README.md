# Subdomain Visit Count

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Counting
**Tags:**

**LeetCode:** [Problem 811](https://leetcode.com/problems/subdomain-visit-count/description/)

## Problem Description

A website domain `"discuss.leetcode.com"` consists of various subdomains. At the top level, we have `"com"`, at the next level, we have `"leetcode.com"` and at the lowest level, `"discuss.leetcode.com"`. When we visit a domain like `"discuss.leetcode.com"`, we will also visit the parent domains `"leetcode.com"` and `"com"` implicitly.

A <strong>count-paired domain</strong> is a domain that has one of the two formats `"rep d1.d2.d3"` or `"rep d1.d2"` where `rep` is the number of visits to the domain and `d1.d2.d3` is the domain itself.

- For example, `"9001 discuss.leetcode.com"` is a <strong>count-paired domain</strong> that indicates that <code>discuss.leetcode.com</code> was visited `9001` times.

Given an array of <strong>count-paired domains</strong> <code>cpdomains</code>, return <em>an array of the <strong>count-paired domains</strong> of each subdomain in the input</em>. You may return the answer in <strong>any order</strong>.

## Examples

### Example 1:

```
Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
```

Explanation: We only have one website domain: `"discuss.leetcode.com"`.
As discussed above, the subdomains `"leetcode.com"` and `"com"` will also be visited. So they will all be visited 9001 times.

### Example 2:

```
Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
```

Explanation: We will visit `"google.mail.com"` 900 times, `"yahoo.com"` 50 times, `"intel.mail.com"` once and `"wiki.org"` 5 times.
For the subdomains, we will visit `"mail.com"` 900 + 1 = 901 times, `"com"` 900 + 50 + 1 = 951 times, and `"org"` 5 times.

## Constraints

- 1 <= cpdomains.length <= 100
- 1 <= cpdomains[i].length <= 100
- cpdomains[i] follows either the "rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>.d3<sub>i</sub>" format or the "rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>" format.
- rep<sub>i</sub> is an integer in the range [1, 10<sup>4</sup>].
- d1<sub>i</sub>, d2<sub>i</sub>, and d3<sub>i</sub> consist of lowercase English letters.
