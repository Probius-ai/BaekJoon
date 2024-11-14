with open("sunmoon.txt", "r",encoding="UTF-8") as file:
    for line in file:
        (num,name,weight,height) = line.strip().split(", ")
        
        height = float(height) / 100
        if (not num) or (not name) or (not weight) or (not height):
            continue
        
        bmi = int(weight) / (height* height)
        
        result = ""
        if 25<=bmi:
            result = "과체중"
        elif 18.5<=bmi:
            result = "정상 체중"
        else:
            result = "저체중"
            
        print(f"{num} {name}, {weight}Kg, {height*100:03.0f}cm, BMI:{bmi:.2f}, {result}")