invest = float(input("Enter your Investment: "))
interest = float(input("Enter expected interest: "))
interest = round((interest/100), 2)
year = eval(input("Enter year: "))
for i in range(year):
    invest = invest + (invest * interest)
print("Money: {:.2f}".format(invest))
