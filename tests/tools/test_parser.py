from leetcode_py.tools.parser import HTMLParser


class TestHTMLParser:
    """Test cases for HTMLParser."""

    def test_clean_html(self):
        """Test HTML tag removal."""
        html = "<p>Hello <code>world</code></p>"
        result = HTMLParser.clean_html(html)
        assert result == "Hello world"

    def test_parse_content_with_examples(self):
        """Test parsing content with examples."""
        html_content = """
        <p>Given an array of integers <code>nums</code>, return indices.</p>

        <p><strong class="example">Example 1:</strong></p>
        <pre>
        <strong>Input:</strong> nums = [2,7,11,15], target = 9
        <strong>Output:</strong> [0,1]
        </pre>

        <p><strong>Constraints:</strong></p>
        <ul>
        <li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
        <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
        </ul>
        """

        result = HTMLParser.parse_content(html_content)

        assert "Given an array of integers nums, return indices." in result["description"]
        assert len(result["examples"]) == 1
        assert result["examples"][0]["number"] == 1
        assert "nums = [2,7,11,15]" in result["examples"][0]["text"]
        assert len(result["constraints"]) == 2
        assert "nums.length" in result["constraints"][0]

    def test_parse_content_new_example_format(self):
        """Test parsing paragraphs-based example format (no <pre> block)."""
        html_content = """<p>You are given an array of integers <code>nums</code>.</p>

<p><strong>Example 1:</strong></p>

<p><strong>Input:</strong> <code>nums = [2,7,11,15], target = 9</code></p>

<p><strong>Output:</strong> <code>[0,1]</code></p>

<p><strong>Example 2:</strong></p>

<p><strong>Input:</strong> <code>nums = [3,2,4], target = 6</code></p>

<p><strong>Output:</strong> <code>[1,2]</code></p>

<p><strong>Constraints:</strong></p>

<ul>
\t<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
</ul>
"""

        result = HTMLParser.parse_content(html_content)

        assert "You are given an array of integers nums." in result["description"]
        assert len(result["examples"]) == 2
        assert result["examples"][0]["number"] == 1
        assert "nums = [2,7,11,15], target = 9" in result["examples"][0]["text"]
        assert "[0,1]" in result["examples"][0]["text"]
        assert result["examples"][1]["number"] == 2
        assert "nums = [3,2,4], target = 6" in result["examples"][1]["text"]
        assert len(result["constraints"]) == 1
        assert "nums.length" in result["constraints"][0]

    def test_parse_test_cases(self):
        """Test parsing test cases."""
        test_cases_str = """[2,7,11,15]
9
[3,2,4]
6"""

        result = HTMLParser.parse_test_cases(test_cases_str)

        assert len(result) == 1
        assert result[0] == ["[2,7,11,15]", "9", "[3,2,4]", "6"]

    def test_parse_empty_content(self):
        """Test parsing empty content."""
        result = HTMLParser.parse_content("")

        assert result["description"] == ""
        assert result["examples"] == []
        assert result["constraints"] == []
