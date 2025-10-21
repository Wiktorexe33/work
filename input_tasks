
def inputs():
 
    robotEyes = input("Please enter a character for the eye \n")

    print("##########")
    print(f"# {robotEyes}    {robotEyes} #")
    print("#   --   #")
    print("##########")
    print("#  /||\\  #")
    print("#   ||   #")
    print("##########")
    print("    /\\   ")
    print("   |  |  ")

    name = input("What is your name? ")
    print(f"It is nice to meet you {name}")


    print("What is your name?")
    name = input()

    print("How old are you (in years)?")
    age = input()

    print("How tall are you (in meters)?")
    height = input()

    print("How much do you weigh (in kilograms)?")
    weight = input()
    bmi = float(weight) / (float(height) ** 2) ## Calculates bmi as long as weight and height are floats
    print(f"{name} you are {age} years old and your bmi is {bmi:.2f}")

def characterstate(lives, energy, shield):
    print(f"Lives: {lives * "♥"}")
    print(f"Energy: {energy * "♦"}")
    print(f"Shield: {shield * "♦"}")

print("Please enter the number of lives")
lives = input()

print("Please enter the energy level.")
energy = input()

print("Please enter the shield level.")
shield = input()
print("Health has been set.")

characterstate(int(lives), int(energy), int(shield))
inputs()