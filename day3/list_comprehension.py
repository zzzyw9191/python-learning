numbers = [3, -2, 7, -5, 0, 8, -1, 4]
positive_numbers = [
    number
    for number in numbers
    if number > 0
]
positive_squares = [
    number ** 2
    for number in numbers
    if number > 0
]
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]
print(f"正数：{positive_numbers}")
print(f"正数的平方：{positive_squares}")
print(f"偶数：{even_numbers}")