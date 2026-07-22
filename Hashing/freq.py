todays_order=[
    "Biryani","Burger","Dosa","Idli","Burger","Biryani","Dosa","Biryani","Burger",
    "Biryani"
]

def count_order(orders):
    freq={}
    for dish in orders:
        if dish in freq:
            freq[dish]=freq[dish]+1
        else:
            freq[dish]=1
    return freq
count=count_order(todays_order)
print(count)