# Найдите сумму цифр трехзначного числа.
n = int(input('Введите трехзначное число: '))
while n // 1000 > 0 :
    print('Число не трехзначное')
    n = int(input('Введите трехзначное число: '))

summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa)
