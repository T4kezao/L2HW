N = int(input("Введите размер списка: "))
a = list(range(1, N+1))
for i in a:
    fact = 1
    for number in range(1, i+1):
        fact = fact * number
    print(number, '->' , fact)