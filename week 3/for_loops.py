# Ask user how many mountains to display
print("How many mountains should I display?")
mountainsToDisplay = int(input())

print("Displaying...")
# Loop to display ascii mountains
for mountain in range(mountainsToDisplay):
    print("   /\  ")
    print("  /  \ ")
    print(" /    \ ")
    print("/      \ ")
    print("--------")
# Output done
print("Done!")

# Ask user for steps to target
print("How far are we from the target?")
stepsToTarget = int(input())

# Loop to count down steps to target
for step in range(stepsToTarget):
    print(str(stepsToTarget - step) + " steps remaining")

# Output target achieved
print("Target achieved!")

# Ask user for brightness level
print("What level of brightness is required?")
level = int(input())

print("Adjusting brightness... \n")
# For loop to output brightness levels
for i in range(2, level + 1, 2):
    print(f"Brightness level:{"*" *i}")