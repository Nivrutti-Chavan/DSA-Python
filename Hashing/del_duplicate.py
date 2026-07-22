user_emails=[
    "nitin@gmail.com",
    "adarsh@gmail.com",
    "niv@gmail.com",
    "amar@gmail.com",
    "nitin@gmail.com",
    "jeet@gmail.com",
    "niv@gmail.com"
    
]

def Remove(emails):
    seen=set()
    unique=[]
    for email in emails:
        if email not in seen:
            unique.append(email)
            seen.add(email)
    return unique
            

clear=Remove(user_emails)
print(clear)