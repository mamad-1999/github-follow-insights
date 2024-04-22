import requests, sys, time, threading

followers = []
following = []
unFollowers = []

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
                sys.stdout.write('\r' + f'{colors.BOLD}{colors.OKGREEN}Loading ' + char)
                sys.stdout.flush()
                time.sleep(0.1)
    animation_thread = threading.Thread(target=animate)
    animation_thread.daemon = True
    animation_thread.start()

def clear_loading_animation():
    sys.stdout.write('\r' + ' ' * 10 + '\r')
    sys.stdout.flush()

def get_users(username, action, list):
    loading_animation()  # Start the loading animation
    page = 1
    try:
        while True:
            response = requests.get(f'https://api.github.com/users/{username}/{action}?page={page}&per_page=100')
            
            if response.status_code == 200:
                users = response.json()
                clear_loading_animation()
                
                
                for user in users:
                    list.append(user.get("html_url"))
                    
                if len(users) < 100:
                    break
                else:
                    page += 1
            else:
                clear_loading_animation()
                print(f"{colors.FAIL}Failed to fetch {action} of {username}. Status code: {response.status_code}")
                break            
    finally:
        clear_loading_animation()  # Clear the loading animation
        return

def find_unFollowers(followers, following):
    for f in following:
        if f not in followers:
            unFollowers.append(f)
            print(f"  {colors.ENDC}{colors.OKBLUE} - {f}")
            
            
def save_outputs(list):
    with open('unFollowers.txt', 'w') as file:
        for f in list:
            file.write(f + '\n')

username = input(f"     {colors.BOLD}Enter your Github Username: ")
print(f"     {colors.ENDC}Do you want to save output (.txt)?")
print(f"     {colors.OKGREEN}1. Yes")
print(f"     {colors.FAIL}2. No")
choice = input(f"     {colors.ENDC}Enter your choice (1 or 2): ")
choice = "Yes" if choice == "1" else "No" if choice == "2" else None
print()

get_users(username, "followers", followers)
print(f"   {colors.BOLD}{colors.OKGREEN}* Total followers: {colors.OKGREEN}{len(followers)}")
get_users(username, "following", following)
print(f"   {colors.BOLD}{colors.OKGREEN}* Total followings: {colors.OKGREEN}{len(following)}")
print()

find_unFollowers(followers, following)
if choice == "Yes":
    save_outputs(unFollowers)
    