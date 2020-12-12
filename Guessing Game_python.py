#a = int(input("Enter the Original Number"))
print("GUESS THE NUMBER BETWEEN 1 TO 50")
print()


a = 24

n = 4

def attempt(n):
    if n == 0:
        pass
    else:
        print("You have",n," attempts to Get the Original number")

def clue(n):
    if n == 3:
        print("Original number is multiple of 2 and 4")
    if n == 2:
        print("Original Number is Not a Square of any Natural Number")
    if n == 1:
        print("Sum of Digits Of original Number is 6")
    

while True:
    attempt(n)
    clue(n)

    if n == 0:
        print("You Lose the Game")
        print("Original Number is",a)
        break
    
    b = int(input("Enter the Guess Number "))

    if b>a:
        print()
        print("This Number is Greater than Original Number")
        print()
        n = n-1

    elif b<a:
        print()
        print("This Number is Less than Original Number")
        print()
        n = n-1

    else:
        print()
        print("Congratulation! You got the Number")
        print()
        break
        
    
    
