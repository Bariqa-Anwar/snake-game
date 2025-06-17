import random

print("""
-----------------Welcome To The-------------------
----------------Snake🐍, Water💧, Gun🔫 Game--------------------- 
""")

computer = random.choice([-1, 0, 1])
me_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

me_str = input("Enter your choice (s/w/g): ").lower()

# Input validation
if me_str not in me_dict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
    exit()

me = me_dict[me_str]

print(f"You chose {reverse_dict[me]}\nComputer chose {reverse_dict[computer]}")

# Game logic (conditions)
if me == computer:
    print("It's a Tie!🤷‍♂️")

elif (computer == -1 and me == 1):
            print("You win🏅")
elif (computer == 1 and me == -1):
            print("You lose!🤦‍♀️")
elif (computer == 0 and me == 1):
            print("You lose!🤦‍♀️")
elif (computer == 0 and me == -1):
            print("You win👑")
elif (computer == -1 and me == 0):
            print("You lose!🤦‍♀️")
elif (computer == 1 and me ==0):
            print("You win👑")
else:
    print("Something went wrong!😐")