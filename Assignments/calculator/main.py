from art import logo
print(logo)
def main():
	operations = {
		"+" : add, 
		"-" : subtract, 
		"*" : multiply, 
		"/" : divide
	}
	num1 = float(input("Enter the first number: "))
	for operator in operations:
		print(operator)
	should_continue =  True
	while should_continue:
		operation_symbol = input("Enter the operator: ")
		num2 = float(input("Enter the next number: "))
		funtionOperation = operations[operation_symbol]
		answer = funtionOperation(num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")

		if input("Do you want to continue? (y/n) ") == "y":
			num1 = answer
		else:
			should_continue = False
			main()
	
#Add
def add(n1, n2):
	return n1 + n2

#Subtract
def subtract(n1, n2):
	return n1 - n2

#Multiply
def multiply(n1, n2):
	return n1 * n2

#Divide
def divide(n1, n2):
	return n1 / n2

if __name__ == "__main__":
	main()