known_users=["Alice","Bob","Charlie","Dan","Emma","Fred","Georgie","Harry"]


while True:
    print( )
    print("Hi! My name is Travis")
    name=input("what is your name?: ").strip().capitalize()
    print( )

    if name in known_users:
        print("Hello {}! how are you?".format(name))
        remove=input("would you like to be removed form the system (y/n)?: ").strip().lower()
        print( )

        if remove =="y":
            known_users.remove(name)
        elif remove=="n":
            print("no problem, I didn't want you to leave anyway :)")
            print( )

    else:
        print("Hmm i don't think I have met you yet {}".format(name))
        add_me=input("would you like to be added to the system (y/n): ").strip().lower()
        if add_me=="y":
            known_users.append(name)
        elif add_me=="n":
            print("No worries, see you around :)")
            print( )
 
