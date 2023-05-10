import coinChange

def innerProd(a, b):
    assert len(a)==len(b)
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
    return sum

coins = [17, 10, 5, 1]
amount = 50

def test():
    nocoin, changes = coinChange.coin_change(coins, amount)
    assert nocoin == 5
    assert amount == innerProd(coins, changes)
