#get user email adress

email= input("What is your email adress? : ").strip()

#slice out user name

user=email[:email.index("@"):]

#slice domain name

domain=email[email.index("@")+1::]

#format message
output_for_user="username :{}".format(user)
output_for_domain="domain :{}".format(domain)

#display output message
print( )
print(output_for_user)
print(output_for_domain)
