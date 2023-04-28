import random

def oddandeven(numbers_list):
    even_numbers = []
    odd_numbers = []
    for num in numbers_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

numbers = (random.randint(1,100) for x in range(0,20))

even_numbers, odd_numbers = oddandeven(numbers)

print(f"Odd: {odd_numbers}")
print(f"Even: {even_numbers}")