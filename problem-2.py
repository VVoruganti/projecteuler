def fib( prev1, prev2, maxVal, curSum):
    sum = curSum
    if (prev2 % 2 == 0):
        sum += prev2
    if (prev1 + prev2 < maxVal):
        return fib(prev2, prev1 + prev2, maxVal, sum)
    else:
        return sum
    
x = fib(1,2,4000000,0)
print(x)


