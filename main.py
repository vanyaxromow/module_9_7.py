# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args):
        fl = 0
        for i in range(2, sum(args) + 1):
            if sum(args) % i == 0:
                fl += 1
        res = 'Простое' if fl == 1 else "Составное"
        print(res)
        return func(*args)

    return wrapper


@is_prime
def sum_three(*args):
    res = sum(args)
    return res


result = sum_three(2, 3, 6)
print(result)
