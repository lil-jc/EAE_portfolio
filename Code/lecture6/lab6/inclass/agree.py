from cs50 import get_string

s = get_string("do you agree? ").lower()

if s in ["y", "Y", "yes"]:
    print("agreed.")
elif s in ["N", "n", "no"]:
    print("not agreed.")