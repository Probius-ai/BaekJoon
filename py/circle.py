import turtle
t= turtle.Turtle()

t.shape("turtle")

# t.circle(100)

# t.left(60)
# t.circle(100)

# t.left(60)
# t.circle(100)

# t.left(60)
# t.circle(100)

# t.left(60)
# t.circle(100)

# t.left(60)
# t.circle(100)
# #=====================================================
# for _ in range(12):
#     t.left(15)
#     t.circle(100)
#     t.left(15)
#     t.circle(50)
# # ========================================
# t.penup()
# t.goto(-200,0)
# t.pendown()

# for i in range(3):
#     t.forward(100)
#     t.left(120)
    
# t.penup()
# t.goto(0,0)
# t.pendown()

# for i in range(4):
#     t.forward(100)
#     t.left(90)
    
# t.penup()
# t.goto(200,0)
# t.pendown()

# t.circle(50)

# # for i in range(5):
# #     t.forward(100)
# #     t.left(360/5)
    
# t.penup()
# t.goto(200,200)
# t.pendown()

# for i in range(18):
#     t.forward(40)
#     t.left(360/18)
    
# t.penup()
# t.goto(-200,200)
# t.pendown()
    
# # t.circle(40)
# #=========================================

# t.penup()
# t.goto(-400,0)
# t.pendown()

# t.forward(800)

# t.penup()
# t.goto(-250,0)
# t.pendown()

# for _ in range(2):
#     t.left(90)
#     t.forward(200)

#     t.left(90)
#     t.forward(15)
    
# t.penup()
# t.goto(-257.5,200)
# t.pendown()

# for _ in range(7):
#     t.circle(50)
#     t.left(360/7)
    
# t.penup()
# t.goto(250,0)
# t.pendown()

# for _ in range(2):
#     t.left(90)
#     t.forward(200)

#     t.left(90)
#     t.forward(15)
    
# t.penup()
# t.goto(242.5,200)
# t.pendown()

# for _ in range(7):
#     t.circle(50)
#     t.left(360/7)
    

# t.penup()
# t.goto(7.5,0)
# t.pendown()

# for _ in range(2):
#     t.left(90)
#     t.forward(300)

#     t.left(90)
#     t.forward(15)
    
# t.penup()
# t.goto(0,300)
# t.pendown()

# for _ in range(7):
#     t.circle(70)
#     t.left(360/7)

# #=================================

n= int(turtle.textinput("", "원하는 n각형"))

for i in range(n):
    t.forward(5)
    t.left(360/n)
    
turtle.exitonclick()