# this is a challenge created in Python Basic Course
# create a currency converter from dollars to local currency.

dollars = input("Please, enter your amount in dollars: ")
dollars = float(dollars)
dollar_price = 21.5
pesos = round(dollars * dollar_price,2)
print("You have $" + str(pesos) + " pesos")