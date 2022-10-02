def factorial(num):
	# num = int(input("enter a number : "))
	if(num == 1):
		return 1

	else:
		return num*factorial(num-1)
num = 6

if num<0:
	print("The number is negative")

elif num == 0:
	print(num,"'s factorial is 1")

else:
	print(num,"factorial is ",factorial(num))