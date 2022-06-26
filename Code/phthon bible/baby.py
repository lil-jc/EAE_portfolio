from random import choice

qns=["why is the sky blue?: ",
     "why is the swiming pool water blue?: ",
     "why is the water in my cup transparent?: "]
question=choice(qns)
ans=input(question).strip().lower()

while ans!="just because":
    ans=input("why?: ").strip().lower()
    print("oh...okay")
