import turtle, time

def makeTurtle(size,road,visited,turtle_map)-> None:
    turtle.setup(width=800,height=500)
    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()
    t.home()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    mario = ["./image/mario_up.gif","./image/mario_left.gif","./image/mario_down.gif","./image/mario_right.gif"]
    mario_block = "./image/mario_block.gif"
    mario_mush = "./image/mario_mush.gif"
    mario_background2 = "./image/mario_background2.gif"
    for m in mario:
        screen.addshape(m)
    screen.addshape(mario_block)
    screen.addshape(mario_mush)
    screen.bgpic(mario_background2)
    s = 0
    for i in range(12):
        for j in range(12):
            t.goto(i*size,j*size)
            if(turtle_map[i][j] == 1):
                t.shape(mario_block)
                t.stamp()
            if(turtle_map[i][j] == 2):
                t.shape(mario_mush)
                s = t.stamp()
    t.showturtle()
    t.shape(mario[0])
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
        t.shape(mario[k%4])
        time.sleep(0.1)
        t.goto(i*size,j*size)
        c_x, c_y = i,j
        time.sleep(0.1)
    t.color('red')
    t.pensize(5)
    t.clearstamp(s)
    visited.pop()
    print(t_pos)
    t.shape(mario[0])
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
        t.shape(mario[k%4])
        c_x, c_y = x,y
        print(k,t_pos)
        time.sleep(0.1)
        t.goto(x*size,y*size)
        time.sleep(0.1)
    turtle.mainloop()
