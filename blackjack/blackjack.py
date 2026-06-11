import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
restart = True
while restart:
    print(logo)


    cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    dealer_hand = []


    def deal_card():
        return random.choice(cards)


    for i in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    player_sum = sum(player_hand)
    dealer_sum = sum(dealer_hand)
    print(f"Dealer hand: [{dealer_hand[0]},***]")
    print(f"Your hand: {player_hand}")
    print(f"Your score: {player_sum}\n")

    # initial check for blackjack
    if player_sum == 21:
        print("Blackjack. You win.")
        play_again = input("DO you want to play once more?(y/n): ").lower()
        if play_again == "y":
            restart = True
        else:
            restart = False
        



    continue_game = True
    draw_card = input("Type 'y' to draw a card\nType 'n' to stand.(y/n): ").lower()
    while continue_game:
        
        if draw_card == "y":
            player_hand.append(deal_card())
            player_sum = sum(player_hand)
            print(f"Your hand: {player_hand}")
            print(f"Your score: {player_sum}")
            if player_sum > 21:
                print(f"Dealer score: {dealer_sum}")
                print("Bust.You lose")
                play_again = input("DO you want to play once more?(y/n): ").lower()
                if play_again == "y":
                    restart = True
                else:
                    restart = False

            elif player_sum == 21:
                print("You win.")
                play_again = input("DO you want to play once more?(y/n): ").lower()
                if play_again == "y":
                    restart = True
                else:
                    restart = False
            elif player_sum < 21:
                draw_card = input("Type 'y' to draw a card\nType 'n' to stand.(y/n): ").lower()
                if draw_card == 'y':
                    continue_game = True
                else:
                    break
        else:
            break

    print(f"Dealer reveals the card: {dealer_hand}")
    print(f"dealer score: {dealer_sum}")
    while dealer_sum < 17:
        dealer_hand.append(deal_card())
        dealer_sum = sum(dealer_hand)
        dealer_sum = sum(dealer_hand)
        print(f"Dealer draws: {dealer_hand[-1]}")
        print(f"Dealer total: {dealer_sum}")


    if dealer_sum > 21:
            print("You win.")
            
    elif dealer_sum == 21:
            print("you lose")
            
    elif dealer_sum > player_sum and player_sum < 22 and dealer_sum < 22:
            print("You lose.")
            
    else:
        print("Its a tie.")

    play_again = input("DO you want to play once more?(y/n: )").lower()
    if play_again == "y":
        restart = True
    else:
        restart = False
     







