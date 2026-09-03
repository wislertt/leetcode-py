[![tests](https://img.shields.io/github/actions/workflow/status/wislertt/leetcode-py/cd.yml?branch=main&label=tests&logo=github)](https://github.com/wislertt/leetcode-py/actions/workflows/cd.yml)
[![release](https://img.shields.io/github/actions/workflow/status/wislertt/leetcode-py/cd.yml?branch=main&label=release&logo=github)](https://github.com/wislertt/leetcode-py/actions/workflows/cd.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wislertt_leetcode-py&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wislertt_leetcode-py)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=wislertt_leetcode-py&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=wislertt_leetcode-py)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=wislertt_leetcode-py&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=wislertt_leetcode-py)
[![codecov](https://codecov.io/gh/wislertt/leetcode-py/graph/badge.svg?token=TI97VUIA4Z)](https://codecov.io/gh/wislertt/leetcode-py)
[![pypi](https://img.shields.io/pypi/v/leetcode-py-sdk.svg?color=blue)](https://pypi.python.org/pypi/leetcode-py-sdk)
[![downloads](https://static.pepy.tech/personalized-badge/leetcode-py-sdk?period=total&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads)](https://pepy.tech/projects/leetcode-py-sdk)
[![python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue?logo=python)](https://github.com/wislertt/leetcode-py/)
[![Star ⭐](https://img.shields.io/github/stars/wislertt/leetcode-py?style=flat&logo=github&color=ffcc00)](https://github.com/wislertt/leetcode-py)
[![Sponsor 💖](https://img.shields.io/badge/Sponsor-💖-pink?style=flat)](https://github.com/sponsors/wislertt)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/wislertt/leetcode-py@main/docs/img/brand/leetcode-py-lockup-dark.svg">
    <img src="https://cdn.jsdelivr.net/gh/wislertt/leetcode-py@main/docs/img/brand/leetcode-py-lockup.svg" width="360" alt="leetcode-py logo">
  </picture>
</p>

# leetcode-py

A Python package to generate professional LeetCode practice environments: a problem README, a typed solution stub, a parametrized pytest suite with 10+ cases, helpers, and a playground notebook, all from JSON templates. Full documentation lives at [leetcode-py.wisl.dev](https://leetcode-py.wisl.dev).

**What makes this different:**

- 🤖 **[LLM-Assisted Workflow](https://leetcode-py.wisl.dev/contributing/problem-creation)**: Generate new problems instantly with AI assistance
- 🎨 **[Visual Debugging](https://leetcode-py.wisl.dev/practice/visualizations)**: TreeNode, ListNode, and GraphNode render as Graphviz diagrams in Jupyter and clean ASCII in the terminal
- 🧪 **[Production Testing](https://leetcode-py.wisl.dev/practice/testing)**: Comprehensive test suites with edge cases and reproducibility verification
- 🚀 **Modern Python**: PEP 585/604 type hints, uv, and professional tooling
- 📊 **Quality Assurance**: 95%+ test coverage, security scanning, automated linting
- ⚡ **[Powerful CLI](https://leetcode-py.wisl.dev/cli/lcpy)**: Generate problems anywhere with `lcpy` command

## 🚀 Quick Start

Requires **Python 3.10+** and **Graphviz** for visualizations ([install guide](https://graphviz.org/download/)).

```bash
# Install the package
pip install leetcode-py-sdk

# Generate problems anywhere
lcpy gen -n 1                    # Generate Two Sum
lcpy gen -t grind-75             # Generate all Grind 75 problems
lcpy list -t blind-75            # List Blind 75 problems

# Start practicing
cd leetcode/two_sum
python -m pytest test_solution.py  # Run tests
# Edit solution.py, then rerun tests
```

See the [Quickstart](https://leetcode-py.wisl.dev/getting-started/quickstart) for the full walkthrough and the [CLI guide](https://leetcode-py.wisl.dev/cli/lcpy) for every option.

## 🗂️ Collections

<!-- problem-count:start -->1404<!-- problem-count:end --> problems, ready to generate, across seven complete collections. Browse them all in the [catalog](https://leetcode-py.wisl.dev/catalog):

| Collection                                                           | What it is                                                  |
| -------------------------------------------------------------------- | ----------------------------------------------------------- |
| [Grind 75](https://leetcode-py.wisl.dev/catalog/grind-75)            | Essential coding interview questions, time-boxed study plan |
| [Grind](https://leetcode-py.wisl.dev/catalog/grind)                  | 169 problems; Grind 75 plus the extended edition            |
| [Blind 75](https://leetcode-py.wisl.dev/catalog/blind-75)            | The original curated list                                   |
| [NeetCode 150](https://leetcode-py.wisl.dev/catalog/neetcode-150)    | Comprehensive coverage by topic                             |
| [NeetCode 250](https://leetcode-py.wisl.dev/catalog/neetcode-250)    | NeetCode 150 plus 100 more                                  |
| [NeetCode All](https://leetcode-py.wisl.dev/catalog/neetcode)        | The complete neetcode.io list; coverage still growing       |
| [AlgoMaster 75](https://leetcode-py.wisl.dev/catalog/algo-master-75) | Curated algorithmic mastery problems                        |

## 🛠️ Development

```bash
git clone https://github.com/wislertt/leetcode-py.git
cd leetcode-py
uv sync
bake test
```

Problems in `leetcode/` are generated from JSON templates. To add one, use the [LLM-assisted workflow](https://leetcode-py.wisl.dev/contributing/problem-creation); for repo tasks see the [bakefile guide](https://leetcode-py.wisl.dev/contributing/bakefile).

## 📖 Documentation

- [Why leetcode-py](https://leetcode-py.wisl.dev/getting-started/why-leetcode-py)
- [Installation](https://leetcode-py.wisl.dev/getting-started/installation)
- [Problem anatomy](https://leetcode-py.wisl.dev/practice/problem-anatomy)
- [Testing pattern](https://leetcode-py.wisl.dev/practice/testing)
- [Visualizations](https://leetcode-py.wisl.dev/practice/visualizations)
- [Notebook workflow](https://leetcode-py.wisl.dev/practice/notebooks)
- [CLI reference](https://leetcode-py.wisl.dev/cli/lcpy)
- [Contributing](https://github.com/wislertt/leetcode-py/blob/main/CONTRIBUTING.md)

## 💖 Support This Project

If you find this project helpful, please consider **starring the repo ⭐** or **sponsoring my work 💖**.

[![Star ⭐](https://img.shields.io/github/stars/wislertt/leetcode-py?style=flat&logo=github&color=ffcc00)](https://github.com/wislertt/leetcode-py)
[![Sponsor 💖](https://img.shields.io/badge/Sponsor-💖-pink?style=flat)](https://github.com/sponsors/wislertt)

## License

Apache-2.0. See [LICENSE](LICENSE).
