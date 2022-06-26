import sys

names = ["bill", "charlie", "fred", "george", "ginny", "percy", "ron"]

if "ron" in names:
    print("found")
    sys.exit(0)
else:
    print("not found")
    sys.exit(1)