from replit import clear
from art import logo

print(logo)
bid_entry = {}
bid_not_ends = True

def bid_winner(bidder):
	max_bid = 0
	for key in bid_entry:
		if bid_entry[key] > max_bid:
			max_bid = bid_entry[key]
			highest_bidder = key
	print(f"{highest_bidder} is the winner with a bid of ${max_bid}")

while bid_not_ends:
	name = input("What is your name?: ")
	bid = int(input("What's your bid?: $"))
	bid_entry[name] = bid
	repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n")
	if repeat.lower() == "no":
		bid_not_ends = False
		bid_winner(bid_entry)
	else:
		clear()