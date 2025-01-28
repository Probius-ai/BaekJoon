def triangle(a,b,c):
    if a**2+b**2==c**2:
        print("right")
    else:
        print("wrong")

while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break

    large = max(a,b,c)
    if large == a:
        triangle(b,c,large)
    elif large == b:
        triangle(a,c,large)
    else:
        triangle(a,b,large)