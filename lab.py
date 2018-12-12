'''
Created on 9 dic. 2018

@author: Pedro
'''
import turtle
from random import randint

myPen = turtle.Turtle()
myPen._tracer(0)
myPen.speed
myPen.hideturtle()

def text(message,x,y,size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)              
    myPen.write(message,align="left",font=FONT)

def box(intDim):
    myPen.begin_fill()
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

palette=["#FFFFFF","#000000","#ffff00","#33ff00","#AAAAAA"]
maze =    [[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
maze.append([1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1])
maze.append([1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1])
maze.append([1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,1])
maze.append([1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1])
maze.append([1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1])
maze.append([1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1])
maze.append([1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1])
maze.append([1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1])
maze.append([1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1])
maze.append([1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1])
maze.append([1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1])
maze.append([1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1])
maze.append([1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1])
maze.append([1,0,0,0,1,0,0,0,0,0,1,0,2,1,0,0])
maze.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

def drawMaze(maze):
  boxSize = 30    
  myPen.penup()
  myPen.goto(-250,200)
  myPen.setheading(0)
  for i in range (0,len(maze)):
    for j in range (0,len(maze[i])):
        myPen.color(palette[maze[i][j]])
        box(boxSize)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.pendown()    
    myPen.setheading(270) 
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180) 
    myPen.forward(boxSize*len(maze[i]))
    myPen.setheading(0)
    myPen.pendown()


def exploreMaze(maze, row, col):
    if maze[row][col] == 2:
        return True
    elif maze[row][col] == 0:
        maze[row][col] = 3
        myPen.clear()
        drawMaze(maze) 
        myPen.getscreen().update()        
        if row < len(maze) - 1:
            if exploreMaze(maze, row + 1, col):
                return True
        if row > 0:
            if exploreMaze(maze, row - 1, col):
                return True
        if col < len(maze[row]) - 1:
            if exploreMaze(maze, row, col + 1):
                return True
        if col > 0:
            if exploreMaze(maze, row, col - 1):
                return True
        maze[row][col] = 4    
        myPen.clear()
        drawMaze(maze)
        myPen.getscreen().update()
        print("Regresando")
drawMaze(maze) 
myPen.getscreen().update()
solved = exploreMaze(maze,0,1)
if solved:
    print("Laberinto Resuelto")
    text("Laberinto Resuelto",-100,-150,20)
else:  
    print("No se puede resolver")
    text("No se puede resolver",-130,-150,20)

myPen.getscreen().update()    
