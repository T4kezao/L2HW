a = int(input("Введите целое число: "))
sum = 0
while (a != 0):
    sum = sum + a % 10
    a = a // 10
print("Сумма цифр числа равна: ", sum)