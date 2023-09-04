'''
Простые числа - это числа больше 1, которые 
не имеют делителей, кроме 1 и самих себя. 
Задача состоит в том, чтобы написать программу, которая будет 
находить и выводить все простые числа в заданном диапазоне.

Пример решения:

Программа принимает на вход начальное и конечное числа диапазона.
Для каждого числа в диапазоне проверяется, является ли оно 
простым.
Если число простое, оно добавляется в список простых чисел.
В конце программа выводит список найденных простых чисел.
'''

def is_prime(start_val, end_val):
    prime = []
    for num in range(start_val, end_val + 1):
        is_prime = True
        if num< 2:
            is_prime = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
    return prime


start_val = int(input("Введите начальное значение: "))
end_val = int(input("Введите конечное значение: "))
k = is_prime(start_val, end_val)
print(k)