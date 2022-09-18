print("Welcome to the TAMID Calculator!")

while True:
    question = input("Would you like to calculate something (y/n): ")
    
    #Prompt user to input function and two numbers if they answer yes
    if question == "y":
        num1 = float((input("Please enter the first number: ")))
        num2 = float((input("Please enter the second number: "))) 
        print("Available functions: +, -, /, and %")
        function = input("Please enter your function: ")   
        
        #Add, subtract, multiply, divide, and modulo functions
        if function == "+":
            print("Your result was: ", (num1 + num2), " !")
        elif function == "-":
            print("Your result was: ", (num1 - num2), " !")
        elif function == "*":
            print("Your result was: ", (num1 * num2), " !")
        #If function is division & second number is 0, tell user they can't divide by 0 
        #Prompt them to enter another number
        elif function == "/":
            if num2 == 0:
                print("You cannot divide by 0!")
                new_num2 = float((input("Please enter the second number again: ")))
                print("Your result was: ", (num1 / new_num2), " !")
            else: 
                print("Your result was: ", (num1 / num2), " !")
        elif function == "%":
            print("Your result was: ", (num1 % num2), " !")
        else: 
            print("Invalid function.")
    
    #Stop the code if user answers no
    elif question == "n":
        print("Thanks for coming!")
        break
    else:
        print("Invalid input.")
        