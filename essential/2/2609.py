def prime_factorization(A):
    numbers = []
    d=2
    while d<=A:
        if A % d == 0:
            A /= d
            if d not in numbers:
                numbers.append(d)
        else:
            d += 1
    return numbers

#유클리드 호제법
def gcd(a,b): 
    while b>0:
        a,b = b, a%B
    return a
#(최대공배수*최대공약수) = a*b
def lcm(a,b):
    return a*b/gcd(a,b)

A,B = map(int,input().split())

A,B = max(A,B),min(A,B)
print(gcd(A,B))
print(int(lcm(A,B)))