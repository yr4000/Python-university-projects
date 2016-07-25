def change(amount, coins):

    """
    recursively computes the number of ways
    to make change of a certain amount of money using a given list of coin values
    """    

    if (amount == 0):
        return 1
    elif (amount < 0 or coins == []):
        return 0
    else:
        print("rec")
        return change(amount, coins[:-1]) + change(amount - coins[-1], coins)


def change_fast(amount, coins):
    dic_coins = {}
    return iner_change_fast(amount, coins, dic_coins)

def iner_change_fast(amount, coins, dic_coins):
    coins.sort()
    temp_tup = tuple([amount] + coins)
    print(dic_coins)
    if (amount < 0 or coins == []):
        return 0
    if coins == [1]:
        return 1
    if (amount == 0):
        return 1
    if temp_tup not in dic_coins:
        dic_coins[temp_tup] = iner_change_fast(amount, coins[:-1],dic_coins)\
                              + iner_change_fast(amount - coins[-1], coins,dic_coins)
    return dic_coins[temp_tup]

