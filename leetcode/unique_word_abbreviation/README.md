# Unique Word Abbreviation

**Difficulty:** Medium
**Topics:** Design, Array, Hash Table, String
**Tags:**

**LeetCode:** [Problem 288](https://leetcode.com/problems/unique-word-abbreviation/description/)

## Problem Description

The **abbreviation** of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an **abbreviation** of itself.

For example:

- `dog -> d1g` because there is one letter between the first letter `d` and the last letter `g`.
- `internationalization -> i18n` because there are 18 letters between the first letter `i` and the last letter `n`.
- `it -> it` because any word with only two characters is an **abbreviation** of itself.

Implement the `ValidWordAbbr` class:

- `ValidWordAbbr(String[] dictionary)` Initializes the object with a `dictionary` of words.
- `boolean isUnique(string word)` Returns `true` if **either** of the following conditions are met (otherwise returns `false`):
    - There is no word in `dictionary` whose **abbreviation** is equal to `word`'s **abbreviation**.
    - For any word in `dictionary` whose **abbreviation** is equal to `word`'s **abbreviation**, that word and `word` are **the same**.

## Examples

### Example 1:

```
Input
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
Output
[null, false, true, false, true, true]

Explanation
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear"); // return false, "deer" and "dear" share "d2r" but differ.
validWordAbbr.isUnique("cart"); // return true, no dictionary word abbreviates to "c2t".
validWordAbbr.isUnique("cane"); // return false, "cake" and "cane" share "c2e" but differ.
validWordAbbr.isUnique("make"); // return true, no dictionary word abbreviates to "m2e".
validWordAbbr.isUnique("cake"); // return true, "cake" is the only word with "c2e".
```

## Constraints

- `1 <= dictionary.length <= 3 * 10^4`
- `1 <= dictionary[i].length <= 20`
- `dictionary[i]` consists of lowercase English letters.
- `1 <= word.length <= 20`
- `word` consists of lowercase English letters.
- At most `5000` calls will be made to `isUnique`.
