def multiply(numbers):  
    total = 1
    for n in numbers:
        total *= n  
    return total  
print(multiply((1, 2, 3, 5, 6)))