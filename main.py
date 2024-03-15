import time

def find_coins_greedy(amount, coins):
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        num_coins = amount // coin
        if num_coins > 0:
            result[coin] = num_coins
            amount -= num_coins * coin
        if amount == 0:
            break
    return result


def find_min_coins(amount, coins):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    last_coin = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


amount = 1000
coins = [1, 5, 10, 25, 50, 100]

start_time_greedy = time.time()
greedy_result = find_coins_greedy(amount, coins)
end_time_greedy = time.time()
greedy_time = end_time_greedy - start_time_greedy


start_time_min_coins = time.time()
min_coins_result = find_min_coins(amount, coins)
end_time_min_coins = time.time()
min_coins_time = end_time_min_coins - start_time_min_coins

print(greedy_time)
print(min_coins_time)
