dict={}

dict["niv@gmail.com"]="Nivrutti Chavan"
dict["nitin@gmailcom"]="Nitin Pinjari"
dict["amar@gmail.com"]="Amardeep"

print(dict["niv@gmail.com"])
#deleting user
del dict["amar@gmail.com"]
print(dict)
#only see  key
print(dict.keys())
#only values
print(dict.values())
#to see both
print(dict.items())