# ask user for name
name=input("what is your name? :")

# ask user for age
age=input("how old are you? :")

# ask user for city
city=input("which city do you live in? :")

# ask uder what they enjoy
enjoy=input("what is your hobby? :")

# create output text
string="Hi {} you are {} years old. You live in {} and you like {}. Nice to meet you!"
output=string.format(name,age,city,enjoy)

# print output to screen
print( )
print(output)
