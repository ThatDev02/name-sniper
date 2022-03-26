import random
import requests
import json
import threading
import itertools
import string

def check_username(username):
    data = requests.get(f"https://api.roblox.com/users/get-by-username?username={username}").json()
    try:
        data["errorMessage"]
        print(f"{username} is not taken")
        with open("usernames.txt", "a") as myfile:
            myfile.write(username + "\n")
    except:
        print(f"{username} is taken")
        with open("taken.txt", "a") as myfile:
            myfile.write(username + "\n")

def pick_username():
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(5))

        
def program():
    while True:
        check_username(pick_username())

def main():
    for i in range(750):
        threading.Thread(target=program).start()

main()

    
    
    


        


