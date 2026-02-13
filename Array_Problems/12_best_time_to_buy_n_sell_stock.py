# Best time to buy and sell stock

prices = [7,2,1,5,6,4,8]

def fun(prices):
    n = len(prices)
    max_profit = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
    return max_profit 
print("Max frofit he/she will make is: ",fun(prices))
# Time Complexity:  O(n^2)`
#Space Complexity: O(1)



def fun_opt(prices):
    n = len(prices)
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit 
    return max_profit
print("Max profit: ",fun_opt(prices))
# Time Complexity:  O(n)
# Space Complexity: O(1)
