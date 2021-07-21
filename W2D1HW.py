# Exercise 1
num = 1
while num <= 10:
    print(num * num * num)
    num += 1

# Exercise 2
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break
def isPrime(n):
    if n == 1:
        return False
    elif n > 1:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

for n in range(2,100,1):
    if isPrime(n):
       print(n)
    else:
        pass


# Exercise 3
age = int(input("How old are you?"))
if age < 18:
    print("kids")
elif age > 65:
    print("seniors")
else:
    print("adults")
