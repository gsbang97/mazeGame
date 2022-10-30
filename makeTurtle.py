import turtle, time
from copy import deepcopy

def makeTurtle(size,road,visited,turtle_map)-> None:
    #turtle_map = deepcopy(test.test_map1)
    turtle.setup(width=size*50,height=size*50)
    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()
    t.home()
    t.speed(0)
    s = 0
    for i in range(12):
        for j in range(12):
            t.goto(i*size,j*size)
            if(turtle_map[i][j] == 1):
                t.pendown()
                t.dot(size)
                t.penup()
            if(turtle_map[i][j] == 2):
                t.pendown()
                t.color('red')
                s = t.stamp()
                t.penup()
                t.color('black')
    t.goto(size,size)
    t.color('blue')
    t.pendown()
    t.speed(10)
    t_pos = 3
    c_x, c_y = 1,1
    for i,j in road:
        if c_x - i == 1:
            k = 1 
        elif c_y - j == 1:
            k = 2
        elif c_x - i == -1:
            k = 3
        else :
            k = 4
        
        t.right((t_pos-k)*90)
        t_pos = k
        time.sleep(0.1)
        t.goto(i*size,j*size)
        c_x, c_y = i,j
        time.sleep(0.1)
    t.color('red')
    t.pensize(5)
    t.clearstamp(s)
    visited.pop()
    print(t_pos)
    while visited:
        x,y = visited.pop()
        k = 0
        d = [visited.index([i,j]) for i,j in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)] if [i,j] in visited ]
        if d:
            visited = visited[:min(d)+1]
        if c_x - x == 1:
            k = 1 
        elif c_y - y == 1:
            k = 2
        elif c_x - x == -1:
            k = 3
        else :
            k = 4
        c_x, c_y = x,y
        print(k,t_pos)
        t.right((t_pos-k)*90)
        t_pos = k
        time.sleep(0.1)
        t.goto(x*size,y*size)
        time.sleep(0.1)
    turtle.mainloop()
