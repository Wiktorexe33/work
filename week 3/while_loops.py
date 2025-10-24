# Ask user for number of apples to be removed
print("How many apples should I remove?")
applesToRemove = int(input())
# Declare a counter variable
applesRemoved = 0

# Remove apples using a while loop
while applesRemoved < applesToRemove:
    print("Removed apple.")
    applesRemoved = applesRemoved + 1

# Ask user for the amount of obstacles to be avoided
print("How many obstacles should I avoid?")
obstaclesToAvoid = int(input())
# Declare a counter variable
obstaclesAvoided = 0
# Avoid obstacles using a while loop
while obstaclesAvoided < obstaclesToAvoid:
   
    obstaclesAvoided = obstaclesAvoided + 1
    print("Avoiding...Done! " + str(obstaclesAvoided) + " obstacles avoided.")
print("All obstacles have been avoided.")


# Ask user for amount of bars to charge
print("How many bars should be charged?")
barsToCharge= int(input())
# Declare a counter variable
barsCharged = 0
# Output bars being charged
while barsCharged < barsToCharge:
    barsCharged = barsCharged + 1
    print(f"Charging: {"█" * barsCharged}")

print("The battery is fully charged.")

# Ask user to enter a phrase
print("Please enter a phrase:")
phrase = input()
# Output Hi repeated as many times as the length of the phrase
print("Hi " * len(phrase)) 

# Set up counter and total variables
counter = 0
total = 0

# Output to indicate start of calculation
print("Calculating the sum of the first 100 numbers...")
# Loop to calculate the sum
while counter != 100:
    counter += 1
    total += counter
# Output the result
print("...Done! The answer is", total)