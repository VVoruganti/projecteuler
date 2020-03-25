def prime(x):
    limit = round(x/2)
    for i in range(2, limit+1):
        if(x % i != 0):
            return False
    return True

primes = [ ] 

counter = 2 
while (len(primes) < 10001 ):
    if(prime(counter)):
        primes.append(counter)
    counter+= 1


print(primes[-1])
