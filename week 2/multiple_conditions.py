# Ask user for adventure type
print("What type of adventure should I have?")
adventureType = input()

# Determine what to output based on multiple conditions
if (adventureType == "scary") or (adventureType == "short"):
    print("Entering the dark forest!")
elif (adventureType == "safe") or (adventureType== "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")