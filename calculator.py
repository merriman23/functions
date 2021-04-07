# Get information from the user
# TODO user input validation for menu
# TODO user input validation for number
# user input on the type of conversion
# user enters in to convert in to mm, mm for mm to in
# user enters 1 for in to mm, 2 for mm to in
userConversionInput = input("What type of conversion \n\t1-inches to mm \n\t2-mm to inches: ")

userInput = input("What is your number: ")

userNumber = float(userInput)

def calculate(number, conversionType):
    if conversionType == '1':
        print('inches to mm')
        answer = number * 25.4
    if conversionType == '2':
        print('mm to inches')
        answer = number / 25.4
    return answer

def printResults(userConversionInput, userInput, userAnswer):
    if userConversionInput == '1':
        conversionUnit = 'in'
        convertedUnit = 'mm'
    if userConversionInput == '2':
        conversionUnit = 'mm'
        convertedUnit = 'in'
    print(userInput,conversionUnit,'=',userAnswer,convertedUnit)
    

print(type(userInput)) 


userAnswer = calculate(userNumber,userConversionInput)
printResults(userConversionInput,userInput,userAnswer)



# Print out the answer to the user
print("The answer is:", userAnswer)