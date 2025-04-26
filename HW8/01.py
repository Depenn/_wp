def big(numbers):
    m = numbers[0]
    for n in numbers:
        if n > m:
            m = n
    return m
    
print(big([3,1,4,2,8,5]))
