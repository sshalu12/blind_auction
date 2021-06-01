# Blind Auction
# There is an auction in which auction amount of bidders are hidden . At last the one which has highest auction amount will win.

from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program. ")
ends= True
auction={}
while ends:
  name=input("What is your name? : ")
  bid=int(input("What's your bid? : $"))
  auction[name]=bid
  k=input("are there any other bidders? Type 'yes' or 'no'. ").lower()
  if k=="yes":
    clear()
  else:
    ends=False

highest_bid=0
for key,value in auction.items():
  
  if (value>highest_bid):
    highest_key=key
    highest_bid=value
print(f"The winner is {highest_key} with a bid of ${highest_bid}.")  
