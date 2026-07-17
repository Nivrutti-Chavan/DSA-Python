def clean(names):
    left=0
    for right in range(1,len(names)):
        if names[left]!=names[right]:
            left+=1
            names[left]=names[right]
    return left+1


names=["aman","aman","diya","chirag","chirag","niv"]
count=clean(names)
print(names[:count])