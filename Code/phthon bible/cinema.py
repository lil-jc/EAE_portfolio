movie={
    "Finding Dory":{"min_age":3,"seats_avail":50},
    "Endgame":{"min_age":16,"seats_avail":50},
    "Venom":{"min_age":16,"seats_avail":3},
    "Fast And Furious":{"min_age":13,"seats_avail":50}
    }
while True:
    print()
#get user's movie of choice    
    choice=input("What movie do you like to watch?: ").strip().title()

    if choice in movie:
        age=int(input("How old are you?: ").strip())
        
#check user's age note the availability of seats
        if age >= movie[choice]["min_age"]:
            
            if movie[choice]["seats_avail"]>0:
                print("enjoy the movie")
                movie[choice]["seats_avail"]=movie[choice]["seats_avail"]-1
            elif movie[choice]["seats_avail"]<=0:
                print("Sorry we don't have any more seats left for {}".format(choice))
                
        if age < movie[choice]["min_age"]:
            print("Sorry you did not met the age requiment, you can't watch the movie" )

    else:
        print("Sorry we don't have that movie")
