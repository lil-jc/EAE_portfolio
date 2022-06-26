students={
    "male":["Tom","Charlie","Harry","Frank"],
    "female":["sarah","Huda","Samantha","Emily","Elizabeth"]
    }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)

