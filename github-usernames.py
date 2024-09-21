
import requests

# GitHub Personal Access Token
GITHUB_TOKEN = 'YOUR_GITHUB_PERSONAL_ACCESS_TOKEN'

# Define a function to check if a username exists on GitHub
def check_github_username(username):
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {'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'}"
    }
    response = requests.get(url, headers=headers)
    
    # If response status code is 404, the username does not exist
    if response.status_code == 404:
        return True  # Username is available
    elif response.status_code == 403:
        print("Rate limit exceeded or access forbidden. Please check your token.")
        return None
    else:
        return False  # Username is taken

# Generate all possible 4-letter usernames using only the letters from 'aljohn'
def generate_usernames():
    letters = 'aljohn'  # Restrict to letters from 'aljohn'
    usernames = []
    
    # Create all combinations of 4 letters using only 'aljohn'
    for first in letters:
        for second in letters:
            for third in letters:
                for fourth in letters:
                    username = first + second + third + fourth
                    usernames.append(username)
    
    return usernames

# Check all 4-letter usernames
def check_all_usernames():
    available_usernames = []
    usernames = generate_usernames()
    
    for username in usernames:
        is_available = check_github_username(username)
        if is_available is None:
            break  # Stop if rate limit or other issue arises
        if is_available:
            print(f"{username} is available")
            available_usernames.append(username)
        else:
            print(f"{username} is taken")
    
    return available_usernames

if __name__ == "__main__":
    # Run the check and print available usernames
    available_usernames = check_all_usernames()
    print("\nAvailable 4-letter GitHub usernames using only 'aljohn':")
    print(available_usernames)

