import coinChange

coins = [500, 101, 9, 1]
amount = 990

def test():
    nocoin, changes = coinChange.coin_change(coins, amount)
    assert nocoin == 18
    assert changes == [0, 9, 9, 0]