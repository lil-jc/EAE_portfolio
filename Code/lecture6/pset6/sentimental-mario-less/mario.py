from cs50 import get_int

# get height of pyramid form user
while True:
    height = get_int("Height: ")
    if (height > 0 and height <= 8):
        break

# print the pyramid
for i in range(height):

    print(" " * (height-(i+1)), end="")
    print("#" * (i+1))
