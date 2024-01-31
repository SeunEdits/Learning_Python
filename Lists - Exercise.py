sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
print(sales_w1)
profit = 1.5
sales_w2.append(15)
print(sales_w2)
sales = list(sales_w1) + list(sales_w2)
print(sales)
best_day = max(sales)
worst_day = min(sales)
profit_w1 = sum(sales_w1) * profit
profit_w2 = sum(sales_w2) * profit
profit_best_day = best_day * profit
profit_worst_day = worst_day * profit

print("On my best day, I made $",profit_best_day)
print("On my worst day, I made $", profit_worst_day)
print("In summary, I made $", profit_w1,"on my first week and I made $", profit_w2, "on my second week. Which brings my total made to $", profit_w1 + profit_w2)