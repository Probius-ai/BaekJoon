PI = 3.14

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return "원의 둘레: {}".format(2*PI*radius)

def get_circle_area(radius):
    return f"원의 넓이: {PI*radius*radius:.1f}"