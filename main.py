# 🎯 Goal:
# Write a Python script that asks the user to enter the name of an animal. Then, using a match-case statement, print out the sound that animal makes.
#
# 🔨 Instructions:
# Ask the user to type in one of the following animals:
# "dog", "cat", "cow", "duck", or "lion".
#
# Use a match-case statement to print the correct sound:
#
# dog → "Woof!"
#
# cat → "Meow!"
#
# cow → "Moo!"
#
# duck → "Quack!"
#
# lion → "Roar!"
#
# If the animal is not one of those, use case _: to print:
# "I don't know what sound that animal makes."
#
# 🧠 Hint:
# Use input() to get what the user types in, and remember that strings are case-sensitive — you might want to convert the input to lowercase using .lower().


while True:
    animal = input("Enter the name of an animal (or type 'exit' to quit): ").strip().lower()
    if animal == "exit":
        print("Goodbye!")
        break
    else:
        print(f"You chose: {animal}.")

    match animal:
        case "dog":
            print("Woof!")
        case "cat":
            print("Meow!")
        case "cow":
            print("Moo!")
        case "duck":
            print("Quack!")
        case "lion":
            print("Roar!")
        case "owl":
            print("Twit Twoo!")
        case "donkey":
            print("Hee Haw!")
        case _:
            print("I don't know what sound that animal makes.")
