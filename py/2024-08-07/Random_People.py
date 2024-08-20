# import random

# han01 = list("가나다라마바사아자차카타파하")

# with open("sunmoon.txt","w",encoding="UTF-8") as file:
#     file.write(f"번호\t 이름\t 몸무게\t 키\t     BMI\n")
#     for i in range(1000):
#         name = random.choice(han01) + random.choice(han01) + random.choice(han01)
#         weight = random.randrange(40,100)
#         height = random.randrange(140,200)
#         file.write(f"{i+1:04d},\t {name},\t{weight},\t{height},\t{weight/((height/100)**2):0.2f}\n")
        
# # =============================================================================

import random

han01 = list("가나다라마바사아자차카타파하")

with open("sunmoon.txt","w",encoding="UTF-8") as file:
    for i in range(1000):
        name = random.choice(han01) + random.choice(han01) + random.choice(han01)
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        file.write(f"{i+1:04d}, {name}, {weight}, {height}\n")