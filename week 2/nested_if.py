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
         print("Found some shoes but no phone") # Display message
    else:
        print("Found some mess but no phone.") # Display message
# Check the bathroom
elif place == "in the bathroom":
    print("Where in the bathroom should I look?")
    bathroom_place = input()
    if bathroom_place == "in the bathtub":
        print("Found a rubber duck but no phone") # Display message