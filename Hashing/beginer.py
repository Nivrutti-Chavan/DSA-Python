Input=input("enter gmail:")
users=[
    "amar@gmail.com",
    "nitin@gmail.com",
    "niv@gmail.com"

]

def login():
    for user in users:
        if user==Input:
            print("login suscessfull")
    else:
        print("Cannot find")
login()

#complexity O(n)