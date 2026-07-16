#0th index is static and from next index onwards 
marks=[1,3,5,6,8,11]
Target=13

for i in range(1,len(marks)):
    if marks[0]==Target:
        print("found at index 0")
    elif marks[0]+marks[i]==Target:
        print("Pair",marks[0],marks[i])
    else:
        print("not_found")