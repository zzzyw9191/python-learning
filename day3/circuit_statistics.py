numbers = [12, 7, 18, 5, 20, 9, 16]
total = 0
count = 0
for number in numbers:
    if number%2 == 0:
        total = total + number
        count = count + 1
        print(number)
print(f"偶数总和：{total}")
print(f"偶数数量：{count}")