def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

numbers = [7, 10, 13, 6, 17, 22, 191]
prime_numbers = find_prime_numbers(numbers)
print("Bilangan prima dalam daftar adalah:", prime_numbers)
