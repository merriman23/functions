# Get information from the user
# TODO user input validation
userInput = input("What is your number: ")


userNumber = float(userInput)
print(type(userInput)) 
# Perform the conversion
# Convert in to mm 25.4 mm : 1 in
# Convert from in to mm  (in * 25.4)
userAnswer = userNumber * 25.4

# Convert from mm to in 
userAnswer = userNumber / 25.4

# Print out the answer to the user
print("The answer is: " + userAnswer)