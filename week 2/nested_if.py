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