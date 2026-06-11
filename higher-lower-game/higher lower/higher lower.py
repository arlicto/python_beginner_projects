import random
import art
import game_data
print(art.logo)

def pick_random_item():
    return random.choice(game_data.data)

account_1 = pick_random_item()
account_2 = pick_random_item()
followers_1 = account_1["follower_count"]
followers_2 = account_2["follower_count"]

points = 0
guess_correct = True
while guess_correct:
    print(f"\nCompare A: {account_1["name"]}, a {account_1["description"]}, from {account_1["country"]}")
    print(art.vs)
    print(f"Against B: {account_2["name"]}, a {account_2["description"]}, from {account_2["country"]}")
    guess = input("\nWho has more followers?(A/B)\nYour answer: ").lower()
    if guess == "a" and followers_1 > followers_2:
        points += 1
        print("\n" * 20)
        print(art.correct)
        print(f"Your score: {points}")
        account_2 = pick_random_item()
        followers_1 = account_1["follower_count"]
        followers_2 = account_2["follower_count"]
        
        guess_correct = True
        
    elif guess == "b" and followers_2 > followers_1:    
        points += 1
        print("\n" * 20)
        print(art.correct)
        print(f"Your score: {points}")
        account_1 = account_2
        account_2 = pick_random_item()
        followers_1 = account_1["follower_count"]
        followers_2 = account_2["follower_count"]
        
        guess_correct = True
        
    else:
        print("You lost")
        print(f"Total score: {points}")
        guess_correct = False