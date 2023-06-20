age = eval(input("Enter age: "))
if age == 5:
    print("Go to Kindergarten")
elif age >= 6 and age <= 17:
    print("Go to grade {}".format(age - 5))
elif age > 17:
    print("Go to College")
else:
    print("Too young for school")
