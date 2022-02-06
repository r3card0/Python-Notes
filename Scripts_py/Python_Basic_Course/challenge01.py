# this is a challenge created in Python Basic Course
# create a currency converter from local currency to dollars

pesos = input("Please, enter your amount in pesos mexicanos: ")
pesos = float(pesos) # convert to float
dollar_price = 21.5
dollar = str(round(pesos / dollar_price,2)) # convert to string and round 2 decimals.
print("You have $" + str(dollar) + " dollars")