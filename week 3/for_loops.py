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