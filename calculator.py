# Get information from the user
# TODO user input validation for menu
# TODO user input validation for number
# user input on the type of conversion
# user enters in to convert in to mm, mm for mm to in
# user enters 1 for in to mm, 2 for mm to in
userConversionInput = input("What type of conversion \n\t1-inches to mm \n\t2-mm to inches: ")

userInput = input("What is your number: ")


userNumber = float(userInput)
print(type(userInput)) 
# Perform the conversion
# Convert in to mm 25.4 mm : 1 in
# Convert from in to mm  (in * 25.4)
if userConversionInput == '1':
    userAnswer = userNumber * 25.4
# Convert from mm to in 
if userConversionInput == '2':
    userAnswer = userNumber / 25.4

# Print out the answer to the user
print("The answer is:", userAnswer)