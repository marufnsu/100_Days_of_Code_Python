#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculator!")
bill = float(input("Enter the Bill: "))
number_of_people = int(input("Enter the number of people: "))
tip = float(input("Enter the tip percentage: "))

total_bill = bill + (tip * bill) / 100
bill_per_person = total_bill / number_of_people
rounder_bill_per_person = round(bill_per_person, 2)
print(f"Each person has to pay {rounder_bill_per_person}.")
