# GitHub Follow Analyzer 

[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)](https://www.python.org/downloads/)
[![GitHub Issues](https://img.shields.io/github/issues/mamad-1999/github-follow-insights)](https://github.com/mamad-1999/github-follow-insights/issues)
[![GitHub Stars](https://img.shields.io/github/stars/mamad-1999/github-follow-insights)](https://github.com/mamad-1999/github-follow-insights/stargazers)
[![GitHub License](https://img.shields.io/github/license/mamad-1999/github-follow-insights)](https://github.com/mamad-1999/github-follow-insights/blob/master/LICENSE)


<p>
    <a href="https://skillicons.dev">
      <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Python-Dark.svg" width="48" title="js">
    </a>
</p>

A Python script to analyze your GitHub follow relationships and identify one-way connections where you are following someone, but they are not following you back.

## Features

- Fetches your followers and following lists from the GitHub API
- Compares the two lists to find users that you are following, but they are not following you
- Generates a list of these one-way follow connections
- Colorful command-line output for better readability
- Option to save the output to a text file

## Requirements

- Python 3.6 or later
- `requests` library

## Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/github-follow-analyzer.git

cd github-follow-analyzer

pip install -r requirements.txt

python github-follow-insights.py
```

## Contributing
Contributions are always welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
