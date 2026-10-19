def best_cho(prices,window_size):
    current_total = sum(prices[0:window_size])
    best_total = current_total
    print(f"window_size = {prices[0:window_size]} = {current_total}")
    for i in range (window_size,len(prices)):
        left_chop = prices[i-window_size]
        right_chop = prices[i]
        current_total = current_total-left_chop + right_chop
        window = prices[i-window_size:i]
        print(f"window = {window} ={current_total}")
        if current_total > best_total:
            best_total = current_total
            return best_total
prices = [2,3,4,56,7,8,9]
answer = best_cho(prices,5)
print(answer)