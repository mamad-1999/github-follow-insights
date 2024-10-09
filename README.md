<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue"></a>
  <a href="https://github.com/mamad-1999/github-follow-insights/issues"><img src="https://img.shields.io/github/issues/mamad-1999/github-follow-insights"></a>
  <a href="https://github.com/mamad-1999/github-follow-insights/stargazers"><img src="https://img.shields.io/github/stars/mamad-1999/github-follow-insights"></a>
  <a href="https://github.com/mamad-1999/github-follow-insights/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mamad-1999/github-follow-insights"></a>
</p>

<h4 align="center">A Python script to analyze your GitHub follow relationships and identify one-way connections where you are following someone, but they are not following you back
And, This Python script allows you to unfollow multiple GitHub users programmatically using the GitHub REST API.</h4>
<p align="center">
  <a href="#installation"><img src="https://img.shields.io/badge/Install-blue?style=for-the-badge" alt="Install"></a>
  <a href="#usage"><img src="https://img.shields.io/badge/Usage-green?style=for-the-badge" alt="Usage"></a>
  <a href="#preview"><img src="https://img.shields.io/badge/Preview-red?style=for-the-badge" alt="Preview"></a>
  <a href="#contributing"><img src="https://img.shields.io/badge/Contributing-yellow?style=for-the-badge" alt="Contributing"></a>
</p>
<p align="center">
    <a href="https://skillicons.dev">
      <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Python-Dark.svg" width="48" title="Go">
      <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Github-Dark.svg" width="48" title="github">
    </a>
</p>

### Installation
> [!IMPORTANT]
> #### Requirements
> - Python 3.6 or later

1. Clone the repository:

```bash
git clone https://github.com/yourusername/github-follow-insights.git

cd github-follow-insights

pip install -r requirements.txt
```
> [!IMPORTANT]
> #### Prerequisites For github_unfollower.py Script
> Before using this script, you need to have a GitHub personal access token with the necessary permissions. If you don't have one already, you can generate it [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

### Usage
1. For get the list of users:
```bash
python main.py --token YOUR_GITHUB_TOKEN
```
2. Get and Unfollow the founded users:
```bash
python main.py --token YOUR_GITHUB_TOKEN --unfollow
```
3. For using proxy:
```bash
python main.py --proxy YOUR-PROXY-SERVER --token YOUR_GITHUB_TOKEN --unfollow
```

### Contributing
Contributions are always welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License.
