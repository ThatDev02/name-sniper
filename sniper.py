import random
import string
import requests
import json
import threading
import time



def gen_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))


def gen_dict():
    userDict = {
        "usernames": [],
        "excludeBannedUsers": False
    }
    
    
    for i in range(100):
        userDict["usernames"].append(gen_name())
        
    return userDict
        
        

def check_usernames():
    while True:
        url = "https://users.roblox.com/v1/usernames/users"
        names = gen_dict()
        #print(names)
        data = requests.post(url, names).json()
        try:
            for i in data["data"]:
                foundName = i["requestedUsername"].lower()
                for x in names["usernames"]:
                    if x.lower() == foundName:
                        try:
                            names["usernames"].remove(i["requestedUsername"])
                            
                        except:
                            print("not found user error")
            for user in names["usernames"]:
                print(f"user unclaimed {user}")                    
        except:
            print("ratelimited")
            time.sleep(31)

def main():
    for i in range(1):
        threading.Thread(target=check_usernames).start()
    
main()
    

