import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
should_continue = True

def cesar(orginal_text, shift_amount, encode_or_decode): 
  

  if encode_or_decode == "decode":
    shift_amount *= -1

  shifted = []
  for letter in orginal_text:
    if letter not in alphabet:
      shifted.append(letter)
    else:
      shifted.append(alphabet[(alphabet.index(letter.lower()) + shift_amount) % len(alphabet)])
  print(f"This is the {encode_or_decode}d result: {''.join(shifted)}")


while should_continue:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  cesar(orginal_text=text, shift_amount=shift, encode_or_decode=direction)
  if input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower() == "no":
    should_continue = False
    print("Goodbye")