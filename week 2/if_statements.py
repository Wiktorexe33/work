# Get book from user
print("What type of book is this?")
book = input()
# Check if the book is an adventure book
if book == "adventure":
    print("I like adventure books!")

# Output a finishing message
print("Finished reading book")

# Get activity from user
print("Please enter the activity to be performed.")
activity = input()

# Check if the activity is "calculate"
if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")
# Output a finishing message
print("Activity completed.")

# Get direction from user
print("Towards which direction should I go (up, down, left or right)?")
direction = input()

# Determine movement based on direction
if direction == "up" or direction == "down" or direction == "left" or direction == "right":
    print("I am moving in the " + direction + "ward direction!")
elif direction == "none":
 print("I am not moving!")
else:
 print("Unknown direction!")

# Get a whole number from the user
 print("Please enter a whole number.")
number = int(input())
# Check if the number is even or odd
if number % 2 == 0:
 print(f"The number {number} is an even number.")
else:
 print(f"The number {number} is an odd number.")

# Get two numbers from the user
 print("Please enter the first number.")
 firstNumber = int(input())
 print("Please enter the second number.")
secondNumber = int(input())

# Determine which number is larger
if firstNumber > secondNumber:
 print("The second number is the smallest.")
elif secondNumber > firstNumber:
 print("The first number is the smallest.")
else:
 print("Both are equal!")

 # Get three numbers from the user
print("Please enter the first whole number.")
firstNumber = int(input())
print("Please enter the second whole number.")
secondNumber = int(input())
print("Please enter the third whole number.")
thirdNumber = int(input())

# Determine amount of odd and even numbers
oddCount = 0
evenCount = 0
listofNumbers = [firstNumber, secondNumber, thirdNumber]
for number in listofNumbers:
    if number % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

# Output results
print(f"There were {evenCount} even and {oddCount} odd numbers.")

