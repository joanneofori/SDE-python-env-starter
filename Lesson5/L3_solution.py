def thank_you(name):
  print(f"Dear {name} \nThank you for the graduation gift, it was wonderful!\nLove,\nAndrew\n")

family_gifts = ["Ron", "Christie", "Ashley", "Nick"]
friend_gifts = ["Sam", "Ryan", "Katie", "Amber"]

def print_thank_you_card(names_list):
  for name in names_list:
    thank_you(name)

print_thank_you_card(family_gifts)
print_thank_you_card(friend_gifts)
