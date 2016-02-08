notNum = True
while notNum:
    try:
        x = int(input("Enter a Number "))
        notNum = False
    except ValueError:
        print("Mate, gimme a number")
print ("Your number is",x)