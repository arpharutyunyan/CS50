"""
    Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

    In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
    Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, 
    and ignore any integer that isn’t an accepted denomination.
    
"""

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
