alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# h -> j
def caesar(original_text, shift_amount, choice):
    cipher_text= ""
    if choice == "decode":
            shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
             cipher_text += letter
        else:
            shifted_index = alphabet.index(letter) + shift_amount
            shifted_index = shifted_index % len(alphabet)
            cipher_text +=  alphabet[shifted_index]
        
    print(f"The {direction}d text: {cipher_text}") 

should_continue = True
while should_continue:
    direction = input("Encode or Decode:\n").lower()
    text = input("Type the message:\n").lower()
    shift = int(input("Enter shift value:\n"))



    caesar(original_text= text, shift_amount = shift, choice = direction)

    continue_game = input("Type 'yes' to continue or 'no' to End.")

    if continue_game == "no":
         should_continue = False
         print("Goodbye.")




    
