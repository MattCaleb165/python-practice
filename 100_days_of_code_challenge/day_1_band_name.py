print("Welcome to your personal band name generator!\n\n")

#Grab the user's hometown
raw_hometown = input("What city were you born in? ")
hometown = raw_hometown.capitalize()
print("\n\nNice! Your hometown is " + hometown + "!\n\n")

#Get their pet's name
raw_pet_name = input("What was your childhood pet's name? ")
pet_name = raw_pet_name.capitalize()
print("\n\n" + pet_name + "? That's a great name!\n\n")

print("Your ideal band name is: " + hometown + " " + pet_name + "!")