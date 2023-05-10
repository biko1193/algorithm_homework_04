def coin_change(coins, amount):
    coindc = []
    for i in coins:
        count = 0
        while amount >= i:
            amount -= i
            count += 1
        coindc.append(count)

    dp = sum(coindc)
    return dp, coindc

coins = [100, 10, 5, 1]
amount = 702
print(coin_change(coins, amount))
