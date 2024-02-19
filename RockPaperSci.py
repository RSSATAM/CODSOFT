import random
States = ['Rock','Paper','Scissors']
playAgain = True
while playAgain:
    User = str(input("Choose your play: "))
    try:
        User = States.index(User)
    except: 
        print('Your choice is not one of the choices in Rock, Paper, Scissors')
        break
    Comp = random.randint(0,2)
    winner = (Comp-User)%3
    if winner==0:
        print("There is a tie. Both User and Computer chose " + States[User])
    elif winner==1:
        print("Computer wins. Computer chose "+States[Comp]+" and User chose "+States[User])
    else:
        print("User wins. Computer chose "+States[Comp]+" and User chose "+States[User])
    if str(input("Do you want to play again? (Y/N)")) == "N":
        playAgain = False
print("Thanks for playing!")
