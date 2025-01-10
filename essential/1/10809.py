usr_input = input()
alphabet = [-1]*26

for i in range(len(usr_input)):
    num = ord(usr_input[i])-97
    if alphabet[num] == -1:
        alphabet[num] = i

for i in alphabet:
    print(i,end=" ")