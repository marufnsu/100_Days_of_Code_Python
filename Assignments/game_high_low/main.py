from art import logo, vs
from game_data import data
import random
from replit import clear

def data_format(choice):
	name = choice['name']
	description = choice['description']
	country = choice['country']
	return f"{name}, a {description}, from {country}"

def answer_check(guess, followers_A, followers_B):
	if followers_A > followers_B:
		return guess == 'A'
	else:
		return guess == 'B'

def main():
	print(logo)
	final_score = 0
	continue_game = True
	choice_A = random.choice(data)
	choice_B = random.choice(data)

	while continue_game:
		choice_A = choice_B
		choice_B = random.choice(data)

		while choice_A == choice_B:
			choice_B = random.choice(data)

		print(f"Compare A: {data_format(choice_A)}.")
		print(vs)
		print(f"Against B: {data_format(choice_B)}.")

		guess = input("Who has more followers? Type 'A' or 'B': ").upper()
		followers_A = choice_A['follower_count']
		followers_B = choice_B['follower_count']
		is_right = answer_check(guess, followers_A, followers_B)

		clear()
		print(logo)
		if is_right:
			final_score += 1
			print(f"You're right! Current score: {final_score}.")
		else:
			continue_game = False
			print(f"Sorry, that's wrong. Final score: {final_score}.")

if __name__ == "__main__":
	main()