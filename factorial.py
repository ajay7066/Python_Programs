def factorial():
	num = int(input("enter a number : "))
	if(num == 1):
		return 1

	else:
		return factorial(factorial*(num-1))

factorial()