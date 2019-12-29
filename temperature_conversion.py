#Convert fahrenheit temperature to celsius
#Formula: (FAHRENHEIT - 32) * 5/9
def fahrenheit_to_celsius(temp):
    try:
        return (temp - 32) * (5/9)
    except TypeError:
        return "Your input must be a numerical type (int, double etc.)"
#Convert celsius temperature to fahrenheit
#Formula: (CELSIUS * 9/5) + 32
def celsius_to_fahrenheit(temp):
    try:
        return (temp*(9/5)) + 32
    except TypeError:
        return "Your input must be a numerical type (int, double etc.)"

    
print(fahrenheit_to_celsius("100"))
print(celsius_to_fahrenheit(37.77777777777778))
