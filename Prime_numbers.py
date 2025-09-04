def prime_numbers(n1, n2):
    prime = []
    for num in range(n1, n2+1):
        is_prime=0
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    is_prime=1
                    break
            if is_prime==0:
                prime.append(num)
    return prime
range1=int(input())
range2=int(input())
result=prime_numbers(range1, range2)
print(result)