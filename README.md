# GitHub Follow Analyzer & Unfollower 

[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)](https://www.python.org/downloads/)
[![GitHub Issues](https://img.shields.io/github/issues/mamad-1999/github-follow-insights)](https://github.com/mamad-1999/github-follow-insights/issues)
[![GitHub Stars](https://img.shields.io/github/stars/mamad-1999/github-follow-insights)](https://github.com/mamad-1999/github-follow-insights/stargazers)
[![GitHub License](https://img.shields.io/github/license/mamad-1999/github-follow-insights)](https://github.com/mamad-1999/github-follow-insights/blob/master/LICENSE)


<p>
    <a href="https://skillicons.dev">
      <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Python-Dark.svg" width="48" title="js">
    </a>
</p>

A Python script to analyze your GitHub follow relationships and identify one-way connections where you are following someone, but they are not following you back
And, This Python script allows you to unfollow multiple GitHub users programmatically using the GitHub REST API.

## Features

- Fetches your followers and following lists from the GitHub API
- Compares the two lists to find users that you are following, but they are not following you
- Generates a list of these one-way follow connections
- Colorful command-line output for better readability
- Option to save the output to a text file
- unfollow the users list from .txt file whit github api

## Requirements

- Python 3.6 or later
- `requests` library

## Installation & Usage of github-follow-insights.py

1. Clone the repository:

```bash
git clone https://github.com/yourusername/github-follow-analyzer.git

cd github-follow-analyzer

pip install -r requirements.txt

python github-follow-insights.py
```
## Prerequisites For github_unfollower.py Script

Before using github-unfollower script, you need to have a GitHub personal access token with the necessary permissions. If you don't have one already, you can generate it [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## Usage of github_unfollower.py Script

1. Replace the placeholder `YOUR_ACCESS_TOKEN` in the script with your GitHub personal access token.
2. Modify the `unFollowers.txt` file to include the list of GitHub usernames you want to unfollow, with each username on a new line.
3. Run the script by executing the following command in your terminal:
> [!IMPORTANT]
> For using github.unfollower.py, script the unFollowers.txt should contain the username of users you want to unfollow (no url of users page)

```
python github-unfollower.py
```

## Additional Notes

- You can unfollow users by providing a list of usernames directly in the script or by using a `.txt` file containing usernames. The script provided here reads usernames from the `unFollowers.txt` file.
- The script sends a DELETE request to the GitHub API for each username in the list to unfollow them.
- If the unfollow operation is successful, it prints a success message. Otherwise, it prints a failure message along with the HTTP status code.

## Contributing
Contributions are always welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
