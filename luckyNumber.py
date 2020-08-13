#lucky number program

age = input("Enter your age: ")
weight = input("Enter your weight: ")
monthOfBirth = input("Enter two digit month: ")


calc = int(weight) / int(age) * int(monthOfBirth)


total = ("Your lucky # is: " + str(calc))

print(total)
