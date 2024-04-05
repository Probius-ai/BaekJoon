S = input()
alphabet = [-1]*26

for i in range(len(S)):
    num = ord(S[i])-97
    if alphabet[num]== int(-1):
        alphabet[num] = i

for i in alphabet:
    print(i,end=" ")
print("\n",end="")
