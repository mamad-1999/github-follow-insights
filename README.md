# GitHub Follow Analyzer 

[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)](https://www.python.org/downloads/)
[![GitHub Issues](https://img.shields.io/github/issues/yourusername/github-follow-analyzer)](https://github.com/yourusername/github-follow-analyzer/issues)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/github-follow-analyzer)](https://github.com/yourusername/github-follow-analyzer/stargazers)
[![GitHub License](https://img.shields.io/github/license/yourusername/github-follow-analyzer)](https://github.com/yourusername/github-follow-analyzer/blob/master/LICENSE)

๐ A Python script to analyze your GitHub follow relationships and identify one-way connections where you are following someone, but they are not following you back.

## ๐ Features

- ๐ Fetches your followers and following lists from the GitHub API
- ๐ Compares the two lists to find users that you are following, but they are not following you
- ๐ Generates a list of these one-way follow connections
- ๐ Colorful command-line output for better readability
- ๐ Option to save the output to a text file

## ๐ Requirements

- Python 3.6 or later
- `requests` library

## ๐ Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/github-follow-analyzer.git

cd github-follow-analyzer

pip install -r requirements.txt

python github-follow-insights.py
```

## ๐ Contributing
Contributions are always welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## ๐ License
This project is licensed under the MIT License.
