import turtle
def square_x(x,y,length,d):
    t.up()
    t.goto(x,y)
    t.down()
    
    for _ in range(d):
        t.forward(length)
        t.left(360/d)
        
t = turtle.Turtle()
t.shape("turtle")

a = int(turtle.textinput("","시작 좌표(0~100) x:"))
b = int(turtle.textinput("","시작 좌표(0~100) y:"))
c = int(turtle.textinput("","한 변의 길이: "))
d = int(turtle.textinput("","그리고 싶은 도형의 각의 갯수: "))

square_x(a,b,c,d)

turtle.done()