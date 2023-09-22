num = int(input("Give me a number, and I'll tell you all primes between 1 and your number: "))

prime_numbers = []

for i in range(2, num + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)

print("Prime numbers between 1 and", num, "are:")
for prime in prime_numbers:
    print(prime)