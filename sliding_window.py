def best_price(price,window_size):
    current_total=sum(price[0:window_size])
    best_total=current_total
    print(f"window1:={price[0:window_size]}={current_total}")

    for i in range(window_size,len(price)):
        left_side=price[i-window_size]
        right_side=price[i]
        current_total=current_total-left_side+right_side
        window=price[i-window_size+1:i+1]
        print(f"window={window}={current_total}")

        if current_total>best_total:
            best_total=current_total
    return best_total

price=[2,4,6,1,7,3,5]
answer=best_price(price,3)
print("best answer is :",answer)
