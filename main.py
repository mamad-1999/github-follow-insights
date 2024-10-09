import requests
import sys
import time
import threading
import argparse

followers = []
following = []
unFollowers = []

# Hardcoded path to the exclusion file
exclusion_file_path = './excluded_users.txt'


def load_excluded_users(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{colors.FAIL}Exclusion file not found at {file_path}. Continuing without exclusions.{colors.ENDC}")
        return []

# ANSI color escape codes


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def loading_animation():
    def animate():
        while True:
            for char in '|/-\\':
                sys.stdout.write(
                    '\r' + f'{colors.BOLD}{colors.OKGREEN}Loading ' + char)
                sys.stdout.flush()
                time.sleep(0.1)
    animation_thread = threading.Thread(target=animate)
    animation_thread.daemon = True
    animation_thread.start()


def clear_loading_animation():
    sys.stdout.write('\r' + ' ' * 10 + '\r')
    sys.stdout.flush()


def get_users(username, action, list, content, proxy, access_token):
    loading_animation()  # Start the loading animation
    page = 1
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github+json'
    }
    try:
        while True:
            url = f'https://api.github.com/users/{username}/{action}?page={page}&per_page=100'
            proxies = {"http": proxy, "https": proxy} if proxy else None
            response = requests.get(url, headers=headers, proxies=proxies)

            if response.status_code == 200:
                users = response.json()
                clear_loading_animation()

                for user in users:
                    if content == 'USERNAME':
                        list.append(user.get("login"))
                    else:
                        list.append(user.get("html_url"))

                if len(users) < 100:
                    break
                else:
                    page += 1
            else:
                clear_loading_animation()
                print(
                    f"{colors.FAIL}Failed to fetch {action} of {username}. Status code: {response.status_code}")
                break
    finally:
        clear_loading_animation()  # Clear the loading animation
        return


def find_unFollowers(followers, following, excluded_users):
    for f in following:
        if f not in followers and f not in excluded_users:
            unFollowers.append(f)
            print(f"  {colors.ENDC}{colors.OKBLUE} - {f}")


def save_outputs(list):
    with open('unFollowers.txt', 'w') as file:
        for f in list:
            file.write(f + '\n')


def unfollow_users(unFollowers, access_token):
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github+json'
    }

    for username in unFollowers:
        url = f'https://api.github.com/user/following/{username}'
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            clear_loading_animation()
            print(f'{colors.OKGREEN}Unfollowed {username} successfully{colors.ENDC}')
        else:
            clear_loading_animation()
            print(
                f'{colors.FAIL}Failed to unfollow {username}. Status code: {response.status_code}{colors.ENDC}')


def main():
    # Argument parsing
    parser = argparse.ArgumentParser(
        description='GitHub Followers/Following Tracker with Proxy and Unfollow Support')
    parser.add_argument('--proxy', type=str,
                        help='Proxy server address (e.g., http://0.0.0.0:8086)')
    parser.add_argument('--unfollow', action='store_true',
                        help='Automatically unfollow users after finding them')
    parser.add_argument(
        '--token', type=str, help='GitHub personal access token for authentication and unfollowing users', required=True)
    args = parser.parse_args()

    proxy = args.proxy
    access_token = args.token

    username = input(f"{colors.BOLD}Enter your Github Username: ")
    print(f"{colors.ENDC}Do you want to save output (.txt)?")
    print(f"{colors.BOLD}1. Yes")
    print(f"{colors.BOLD}2. No")
    choice = input(f"{colors.ENDC}Enter your choice (1 or 2): ")
    choice = "Yes" if choice == "1" else "No" if choice == "2" else None
    content_of_text = "USERNAME"
    print()

    # Load excluded users from the hardcoded exclusion file
    excluded_users = load_excluded_users(exclusion_file_path)

    get_users(username, "followers", followers,
              content_of_text, proxy, access_token)
    print(f"{colors.BOLD}{colors.OKGREEN}* Total followers: {colors.OKGREEN}{len(followers)}")
    get_users(username, "following", following,
              content_of_text, proxy, access_token)
    print(f"{colors.BOLD}{colors.OKGREEN}* Total followings: {colors.OKGREEN}{len(following)}")
    print()

    find_unFollowers(followers, following, excluded_users)
    save_outputs(unFollowers)

    # Unfollow users if the --unfollow switch is used
    if args.unfollow:
        unfollow_users(unFollowers, access_token)


if __name__ == "__main__":
    main()
