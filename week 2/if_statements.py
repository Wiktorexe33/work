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