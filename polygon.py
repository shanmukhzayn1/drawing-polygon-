import turtle 
wn = turtle.Screen()
wn.bgcolor("light yellow")
hey = turtle.Turtle()
hey.speed(5)
num_of_sides = int(input("what  shape would you want")) 
length = 100 
angle = 360 / num_of_sides 
for i in range(num_of_sides): 
  hey.forward(length)
  hey.left(angle)
turtle.done()
