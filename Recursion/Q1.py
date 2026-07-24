def Count_Func(Count):
    if Count==0:
        print("Done")
    else:
        print(f"Total count is {Count} One count is removing")
        Count_Func(Count-1)
Count_Func(3)