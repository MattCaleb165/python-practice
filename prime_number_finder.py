num = int(input("Give me a number and I'll tell you all primes between 1 and your number: "))
factors = []

for i in range(1, num+1):
  if num % i == 0:
    factors.append(i)
    
if len(factors) == 2:
  print("Your number is a prime number!")
else:
  print("Your number is not a prime number!")

print(factors)
