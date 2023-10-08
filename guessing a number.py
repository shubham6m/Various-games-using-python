from random import randint
# this randint function generate a random number between any specific range 
random_number = randint(0,10)
print(random_number)
x = -1
while x!= random_number:
    if x!=-1:
        print("You guessed incorrectly")
    x = int(input("enter a number; "))
print("You guessed correctly")