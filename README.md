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

### Preview
![2024-10-09_15-08](https://github.com/user-attachments/assets/7d67a2ce-6d37-4e0a-81fd-4facdcf4481d)

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
> #### Prerequisites
> Before using this script, you need to have a `GitHub personal access token` with the necessary permissions. If you don't have one already, you can generate it [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

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
> [!NOTE]
> #### Excluded Users
> The script uses a file named `excluded_users.txt` to specify GitHub usernames that should be excluded from the unfollow process. This file should be located in the root directory of the script. Each line of the file should contain a single username. Users listed in this file will be ignored during the unfollow operation.
>
> Example `excluded_users.txt` content:
> ```bash
> tomnomnom
> torvalds
> jadijadi
> ``` 

### Contributing
Contributions are always welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License.
