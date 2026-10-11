L = int(input())
current_sum = 0
count = 0
result_primes = []
number = 2


def is_prime(number):
    """判断一个数是否为质数"""
    if number  < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number  % i == 0:
            return False
    return True



while True:
    if is_prime(number):
        if current_sum +number <= L:
            current_sum += number
            result_primes.append(number )
            count += 1
        else:
            break
    number  += 1

for p in result_primes:
    print(p)
print(len(result_primes))