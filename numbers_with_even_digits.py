#Returns true if x contains only even digits
def check_even_digits(x):
    x_str = str(x)
    even_digits = True
    for i in x_str:
        if (int(i) % 2) != 0:
            even_digits = False
    return even_digits

numbers_list = []
for i in range(100,401):
    if check_even_digits(i) == True:
        numbers_list.append(i)
print(", ".join(str(num) for num in numbers_list))
