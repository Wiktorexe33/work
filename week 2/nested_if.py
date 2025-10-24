# Ask user for book details
print("What type of cover does this book have?")
coverType = input()
# Display output based on cover type and binding
if coverType == "soft":
    print("Is the book perfect bound?")
    perfectBound = input()
    if perfectBound == "yes":
     print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")

# Ask user where to look
print("Where should I look?")
place = input()
# Check the bedroom
if place == "in the bedroom":
    print("Where in the bedroom should I look?")
    bedroom_place = input()
    if bedroom_place == "under the bed":
         print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.") 
# Check the bathroom
elif place == "in the bathroom":
    print("Where in the bathroom should I look?")
    bathroom_place = input()
    if bathroom_place == "in the bathtub":
        print("Found a rubber duck but no phone.") 
    else:
        print("Found bathroom stuff but no phone.") 

# Check the living room
elif place == "in the living room":
    print("Where in the living room should I look?")
    lab_place = input()
    if lab_place == "on the table":
        print("Yes! I found my phone!")
    else:
         print("Found some stuff but no phone.")
# For any other inputs
else:
 print("I do not know where that is but I will keep looking")