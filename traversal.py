#nums=[15,51,45,56,89]

"""#left to right 1
for i in nums:
    print(i)"""

"""#left to right 2
for i in range(len(nums)):
    print(nums[i])
"""

"""#right to left 1
for num in reversed(nums):
    print(num)"""

"""#right to left 2
i=len(nums)-1
for i in range(i,-1,-1):
    print(nums[i])"""

"""#right to left 2
for i in nums[::-1]:
    print(i)"""


marks=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

for row in marks:
    for mark in row:
        print(mark,end=" ")
    print()