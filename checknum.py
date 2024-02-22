def checknum():
    num=int(input("What is your number? "))
    if num > 10 and num < 20:
        print("The number is between 10 and 20")
    elif num < 10 or num == 10:
        print("The number is less than or equal to 10")
    else:
        print("The number is greater than 20")


checknum()