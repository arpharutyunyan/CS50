amount = 50
sum_coin = 0
while amount != 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount = abs(amount - coin)
        sum_coin += coin
        if sum_coin >= 50:
            break
print(f"Change Owed: {amount}")
