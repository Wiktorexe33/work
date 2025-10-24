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