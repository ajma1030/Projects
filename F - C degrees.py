tempF = float(input("What is the temperature in degrees Fahrenheit?:"))

tempC = ((tempF - (float(32)))/1.8)
print("The temperature in Celsius is", tempC)


temp_C = (float(input("Now what's the temp in Celsius?:")))

temp_F = (temp_C * 1.8) + (float(32))
print ("The temperature in Fahrenhit is", temp_F)

if(70.0 < temp_F < 78.0):
    print("It's nice weather today")
else:
    print("The weather isn't so nice today")

print("I think I got it")