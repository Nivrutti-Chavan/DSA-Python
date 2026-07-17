#[10,20,30,40,50]
def two_traversal(numbers,target):
    left=0
    right=len(numbers)-1

    while left<right:
        total=numbers[left]+numbers[right]
        if total==target:
            print([left,right])
            return [numbers[left],numbers[right]]

        elif total>target:
            right=right-1

        elif total<target:
            left=left-1
            #left=left+1

numbers = list(map(int, input("Enter numbers: ").split()))#inputt
target=int(input("enter values:"))
print(two_traversal(numbers,target))
