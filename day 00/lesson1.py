from turtle import*

speed(10)

#we want to point a house 

#step 1: draw a square

width(4)
color("grey")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#end of square

#drawind a door

forward(70)
color("black")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()
#end of drawing door

penup()
goto(200,200)
pendown()

#drawing 

color("black")

begin_fill()

right(150)
forward(200)
left(120)
forward(200)

end_fill()

color("grey")
left(30)
forward(85)

color("green")

begin_fill()

left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)

end_fill()

color("grey")
right(90)
forward(25)
right(90)
forward(200)
right(90)
forward(85)

color("green")
begin_fill()

right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)

end_fill()

exitonclick()