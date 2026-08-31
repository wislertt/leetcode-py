# Parsing A Boolean Expression

**Difficulty:** Hard
**Topics:** String, Stack, Recursion
**Tags:** neetcode

**LeetCode:** [Problem 1106](https://leetcode.com/problems/parsing-a-boolean-expression/description/)

## Problem Description

A <strong>boolean expression</strong> is an expression that evaluates to either <code>true</code> or <code>false</code>. It can be in one of the following shapes:

- <code>&#39;t&#39;</code> that evaluates to <code>true</code>.
- <code>&#39;f&#39;</code> that evaluates to <code>false</code>.
- <code>&#39;!(subExpr)&#39;</code> that evaluates to <strong>the logical NOT</strong> of the inner expression <code>subExpr</code>.
- <code>&#39;&amp;(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)&#39;</code> that evaluates to <strong>the logical AND</strong> of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where <code>n &gt;= 1</code>.
- <code>&#39;|(subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub>)&#39;</code> that evaluates to <strong>the logical OR</strong> of the inner expressions <code>subExpr<sub>1</sub>, subExpr<sub>2</sub>, ..., subExpr<sub>n</sub></code> where <code>n &gt;= 1</code>.

Given a string <code>expression</code> that represents a <strong>boolean expression</strong>, return <em>the evaluation of that expression</em>.

It is <strong>guaranteed</strong> that the given expression is valid and follows the given rules.

## Examples

### Example 1:

```
Input: expression = "&(|(f))"
Output: false
Explanation: First, evaluate |(f) --> f. The expression is now "&(f)". Then, evaluate &(f) --> f. The expression is now "f". Finally, return false.
```

### Example 2:

```
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
```

### Example 3:

```
Input: expression = "!(&(f,t))"
Output: true
Explanation: First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)". Then, evaluate !(f) --> NOT false --> true. We return true.
```

## Constraints

- <code>1 &lt;= expression.length &lt;= 2 * 10<sup>4</sup></code>
- <code>expression[i]</code> is one following characters: <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;&amp;&#39;</code>, <code>&#39;|&#39;</code>, <code>&#39;!&#39;</code>, <code>&#39;t&#39;</code>, <code>&#39;f&#39;</code>, and <code>&#39;,&#39;</code>.
