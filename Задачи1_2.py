a = int(input("Введите начало интервала: "))
b = int(input("Введите конец интервала: "))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True

sum_primes = 0
for i in range(a, b+1):
    if is_prime(i):
        sum_primes += i

print(f"Сумма всех простых чисел в интервале от {a} до {b} равна {sum_primes}.")