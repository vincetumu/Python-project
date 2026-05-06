#number guessing game
#concept used:While loops, functions, if conditions and some difficulty levels
#how the game works
#the computer picks a secret random number(player doesn't see it)
#the player chooses the difficulty:(easy(1-50), medium(1-100), hard(1-200))
#the program gives hints after each wrong guess: 'too high' or 'too low'
#the game counts how many attempts it took
#at the end, give a performance rating based on attempts
#Import a random module:gives whole numbers randomly from a given range(1-50)
#Program
import random
#choose difficulty
def get_difficulty():
    print("Choose Difficulty:")
    print("1 ? Easy (1-50)")
    print("2 ? Medium (1-100)")
    print("3 ? Hard (1-200)")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        return 50
    elif choice == "2":
        return 100
    else:
        return 200

def rate_performance(attempts, max_num):
    chances= 7 if max_num == 50 else 10 if max_num == 100 else 15
    if attempts >= chances // 2:
        return "INCREDIBLE, You barely needed any guesses"
    elif attempts >= chances:
        return "GREAT, You played well"
    else:
        return "Keep practicing, you will get faster"

# The game

print("==================================")
print(" VINCE'S NUMBER GUESSING GAME")
print("==================================")
name=input("Enter your name: ").strip()
max_num = get_difficulty()
secret = random.randint(1,max_num)
attempts = 0

print("I have picked a number between 1 and ", max_num)
while True:
    guess = int(input("Enter your guess: "))
    attempts +=1
    if guess < secret:
        print("Your guess is too low, try higher")
    elif guess > secret:
        print("Your guess is too high, try lower")
    else:
        print("You guessed correctly, the number was ", secret)
        print("Attempts:", attempts)
        print("Rating :", rate_performance(attempts, max_num))
        break