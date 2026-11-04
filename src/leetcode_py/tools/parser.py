"""HTML parsing utilities for LeetCode problem content."""

import re
from typing import Any


class HTMLParser:
    """Parser for LeetCode HTML content."""

    @staticmethod
    def clean_html(text: str) -> str:
        """Remove HTML tags for clean text."""
        return re.sub(r"<[^>]+>", "", text).strip()

    EXAMPLE_HEADER_PATTERN = r'<p><strong(?:\s+class="example")?>Example (\d+):</strong></p>'

    @staticmethod
    def parse_content(html_content: str) -> dict[str, Any]:
        """Parse HTML content to extract description, examples, and constraints."""
        # Extract description (everything before first example or constraints)
        desc_match = re.search(
            r"<p>(.*?)"
            r"(?=<p><strong(?:\s+class=\"example\")?>Example \d+:|<p><strong>Constraints:|$)",
            html_content,
            re.DOTALL,
        )
        description = HTMLParser.clean_html(desc_match.group(1)) if desc_match else ""

        # Extract examples. Two known formats:
        # Old: <p><strong class="example">Example 1:</strong></p><pre>...</pre>
        # New: <p><strong>Example 1:</strong></p> followed by
        #      <p><strong>Input:</strong> ...</p> / <p><strong>Output:</strong> ...</p>
        headers = list(re.finditer(HTMLParser.EXAMPLE_HEADER_PATTERN, html_content))
        examples = []
        for i, match in enumerate(headers):
            section_end = headers[i + 1].start() if i + 1 < len(headers) else len(html_content)
            constraints_pos = html_content.find("<p><strong>Constraints:", match.end())
            if constraints_pos != -1:
                section_end = min(section_end, constraints_pos)

            section = html_content[match.end() : section_end]
            lines = [
                line.strip() for line in HTMLParser.clean_html(section).splitlines() if line.strip()
            ]
            examples.append({"number": int(match.group(1)), "text": "\n".join(lines)})

        # Extract constraints
        constraints_match = re.search(
            r"<p><strong>Constraints:</strong></p>\s*<ul>(.*?)</ul>", html_content, re.DOTALL
        )
        constraints = []
        if constraints_match:
            constraint_items = re.findall(r"<li>(.*?)</li>", constraints_match.group(1))
            constraints = [HTMLParser.clean_html(item) for item in constraint_items]

        return {"description": description, "examples": examples, "constraints": constraints}

    @staticmethod
    def parse_test_cases(test_cases_str: str) -> list[list[str]]:
        """Parse test cases from the exampleTestcases string."""
        if not test_cases_str:
            return []

        # Split by newlines and group into test cases
        lines = [line.strip() for line in test_cases_str.split("\n") if line.strip()]

        # Group lines into test cases
        test_cases = []
        current_case = []

        for line in lines:
            if line.startswith(("[", '"', "-")) or line.isdigit():
                current_case.append(line)
            else:
                if current_case:
                    test_cases.append(current_case)
                    current_case = [line]

        if current_case:
            test_cases.append(current_case)

        return test_cases
