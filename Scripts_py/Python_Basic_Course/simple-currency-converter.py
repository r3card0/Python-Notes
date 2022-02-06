# created in Python Basic Course

pesos = input("Please, enter your amount in pesos colombianos: ")
pesos = float(pesos) # convert to float
dollar_price = 4015
dollar = str(round(pesos / dollar_price,2)) # convert to string and round 2 decimals
print("You have " + str(dollar) + " dollars")