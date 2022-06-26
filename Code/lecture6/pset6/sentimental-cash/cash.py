from cs50 import get_float

# get a imput from user
while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break

cents = round(dollars * 100)
coins = 0

while (cents > 0):
    # count the amount of 25 cents
    if (cents >= 25):
        cents = cents - 25
        coins += 1
    # count the amount of 10 cents
    elif (cents >= 10):
        cents = cents - 10
        coins += 1
    # count the amount of 5 cents
    elif (cents >= 5):
        cents = cents - 5
        coins += 1
    # count the amount of 1 cents
    elif (cents >= 1):
        cents = cents - 1
        coins += 1

# print the number of coins
print(f"{coins}")
