## Create functions to solve the area of a circle, taxes, and temperature
#  @param circleArea              the area of a circle in cm
#  @param totalTaxes              the total amount of taxes owed in U.S. dollars
#  @param celsiusTemperature      the temperature in Celsius


## Area of the circle
#radiusInput = int(input("What is the radius of the circle? \n"))
#areaOfCircle = round(3.141592 * radiusInput ** 2, 2)

#def circleArea(Pi, radiusInput):
#    print("The area of the circle is {} cm2.".format(areaOfCircle))

#Pi = 3.14

#circleArea(Pi, radiusInput)
#print("")


## Amount of taxes owed
#moneyInput = int(input("What is your amount of money? \n"))
#taxRate = float(input("What is the tax rate in decimal? Ex: 0.08 \n"))
#taxOwed = moneyInput + (moneyInput * taxRate)

#def taxAmount(moneyInput, taxRate):
#    print("Your tax amount is ${}.".format(taxOwed))

#taxAmount(taxOwed, taxRate)


## Converting Fahrenheit to Celsius temperature
fahrenheitInput = int(input("What is the temperature in Fahrenheit? \n"))
celsius = round((fahrenheitInput - 32) * (5/9), 4)

def convertion(fahrenheitInput):
    print("The temperature outside in Celsius is {} degrees.".format(celsius))

convertion(fahrenheitInput)