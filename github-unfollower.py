import requests

# Replace with your GitHub personal access token
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# https://docs.github.com/en/rest/users/followers?apiVersion=2022-11-28#unfollow-a-user
headers = {
    'Authorization': f'token {ACCESS_TOKEN}',
    'Accept': 'application/vnd.github+json'
}

# 2 Way -> List of usernames OR .txt file of usernames (is there in previous scripts)

# List of user to unfollow
# users_to_unfollow = ['user1','user2']

# Read usernames from a text file
with open('./unFollowers.txt', 'r') as file:
    users_to_unfollow = [line.strip() for line in file]


# Unfollow each user
for username in users_to_unfollow:
    url = f'https://api.github.com/user/following/{username}'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Unfollowed {username} successfully')
    else:
        print(f'Failed to unfollow {username}. Status code: {response.status_code}')