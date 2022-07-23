# Comillas triples ayudan a crear cadenas de caracterés en varias líneas
# Create a menu of options to select a currency
# emojis -> Windows: windows + ; Mac: ctrl + command + space ; Linux: download (e.g EmojiOne Picker)

menu = int(input("""

Colombia    (1)🇨🇴
México      (2)🇲🇽
Argentina   (3)🇦🇷

Please, select a country : """))

if menu == 1:
    pesos = input("Please, enter your amount in pesos colombianos: ")
    pesos = float(pesos) # convert to float
    dollar_price = 4015
    dollar = str(round(pesos / dollar_price,2)) # convert to string and round 2 decimals
    print("You have $" + str(dollar) + " dollars 😊")

elif menu == 2:
    pesos = input("Please, enter your amount in pesos mexicanos: ")
    pesos = float(pesos) # convert to float
    dollar_price = 21.5
    dollar = str(round(pesos / dollar_price,2)) # convert to string and round 2 decimals
    print("You have $" + str(dollar) + " dollars 😊")

elif menu == 3:
    pesos = input("Please, enter your amount in pesos argentinos ")
    pesos = float(pesos) # convert to float
    dollar_price = 102
    dollar = str(round(pesos / dollar_price,2)) # convert to string and round 2 decimals
    print("You have $" + str(dollar) + " dollars 😊")

else:
    print("Select a correct option")
