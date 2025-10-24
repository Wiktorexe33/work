# Ask user for number of apples
print("How many apples should I remove?")
applesToRemove = int(input())
# Declare a counter variable
applesRemoved = 0

# Remove apples using a while loop
while applesRemoved < applesToRemove:
    print("Removed apple.")
    applesRemoved = applesRemoved + 1