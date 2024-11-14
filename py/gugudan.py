#n단 입력
n= int(input("n을 입력하세요: "))

for i in range(1,10):
    for j in range(2,n+1):
        gugudan =f"{j} x {i} = {j*i}"
        print(gugudan, end="\t")
    print()