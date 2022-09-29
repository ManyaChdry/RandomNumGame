import random

rnumber = input("Type a number: ")
# the value that the user would enter (be it error value or some number) would be stored in form of a string
# what we want is "25" -> 25

if rnumber.isdigit():
    rnumber = int(rnumber)

    if rnumber <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_no = random.randint(0, rnumber) #lower and upper bound both are necessary in rand int
guesses = 0
#python is case sensitive true and True are different! True is boolean!!
while True:
    guesses += 1  
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_no:
        print("You got it!")
        break
    elif user_guess > random_no:
        print("You were above the number!")
    else:
        print("You were below the number!")

#instead of elif the below code could hv also been used but elif is much clearner version!
"""
    else:
        if user_guess > random_no:
            print("You were above the number!")
        else:
            print("You were below the number!")
"""
        
if guesses == 1:
    print("You got it in the 1st guess!") #if using commas  : NO NEED TO ADD SPACES!
#print("You got it in " + str(guesses) + " guesses!") 
else:
    print("You got it in", guesses, "guesses!")


#print(random_no)
#type ctrl c if you get in an infinite loop!

