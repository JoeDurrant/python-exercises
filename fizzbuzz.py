#Performs fizzbuzz on numbers up to specified limit, default is 50
def fizzbuzz(limit = 50):
    for i in range(1,limit+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
