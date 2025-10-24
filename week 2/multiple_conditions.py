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

# Ask user for what they hear and see
print("What did I hear?")
hear = input()
print("What did I see?")
see = input()
# Determine what to output based on hear and see
if (hear == "grr") and (see == "two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")