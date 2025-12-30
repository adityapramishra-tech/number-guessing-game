import getpass
print("Select The Number 1 To 100.")
User1 = int(getpass.getpass("Enter your secret number (hidden): "))
User2 = int(input("Enter Your Number : "))
Count = 0
while True:
    Count += 1
    if User2 == User1:
       print("You are founded and You win")
       break
    elif User2 >= User1:
       print("You are more than the win value :")
       print("Do the task first then input the number")
       User2 = int(input("Enter your Number : "))
    elif User2 <= User1:
        print("You are Less than the win value :")
        print("Do the task first then input the number")
        User2 = int(input("Enter your Number : "))
    
print("Number Of gusssin times :",Count)