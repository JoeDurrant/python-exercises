#Returns True if x is prime, False if not prime
def is_prime(x):
    if x <= 1:
        return False #Negative numbers and 1 are not prime
    else:
        for i in range(2,x):# range(2,2) returns an empty list so 2 is seen as prime
            if x % i == 0:
                return False
    return True #If this is reached then no factors have been found

print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))
print(is_prime(10))
print(is_prime(11))
