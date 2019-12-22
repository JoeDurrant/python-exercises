#Convert fahrenheit temperature to celsius
#Formula: (FAHRENHEIT - 32) * 5/9
def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5/9)

#Convert celsius temperature to fahrenheit
#Formula: (CELSIUS * 9/5) + 32
def celsius_to_fahrenheit(temp):
    return (temp*(9/5)) + 32

    
print(fahrenheit_to_celsius(100))
print(celsius_to_fahrenheit(37.77777777777778))
