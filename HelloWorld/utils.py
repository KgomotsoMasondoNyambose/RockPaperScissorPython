def find_max(numbers):
    maximum = 0
    for number1 in numbers:
        if number1 > maximum:
            maximum = number1
    return maximum