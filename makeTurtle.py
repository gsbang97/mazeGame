import turtle, time
def where_go(c_x,c_y,x,y)->int:
    if c_x - x == 1:
        return 1 
    elif c_y - y == 1:
        return 2
    elif c_x - x == -1:
        return 3
    else :
        return 0
def makeTurtle(size,road,visited,turtle_map)-> None:
    turtle.setup(width=800,height=500)
    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()
    t.home()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    mario_jump = ["./image/mario_jump.gif","./image/mario_jump2.gif"]
    mario_king_jump = ["./image/mario_king_jump.gif","./image/mario_king_jump2.gif"]
    mario_king = ["./image/mario_king1.gif","./image/mario_king2.gif","./image/mario_king3.gif"]
    mario = ["./image/mario_up.gif","./image/mario_left.gif","./image/mario_down.gif","./image/mario_right.gif"]
    mario_block = "./image/mario_block.gif"
    mario_mush = "./image/mario_mush.gif"
    mario_background2 = "./image/mario_background.gif"
    for m in mario:
        screen.addshape(m)
    for m in mario_king:
        screen.addshape(m)
    for m in mario_king_jump:
        screen.addshape(m)
    for m in mario_jump:
        screen.addshape(m)
    screen.addshape(mario_block)
    screen.addshape(mario_mush)
    screen.bgpic(mario_background2)
    s = 0
    for i in range(12):
        for j in range(12):
            t.goto(i*size,j*size)
            if(turtle_map[i][j] == -1):
                t.shape(mario_block)
                t.stamp()
            if(turtle_map[i][j] == 2):
                t.shape(mario_mush)
                s = t.stamp()
    t.showturtle()
    t.shape(mario[3])
    t.goto(size,size)
    t.color('blue')
    t.pendown()
    t.speed(10)
    t_pos = 3
    c_x, c_y = 1,1
    for x,y in road[1:]:
        w = where_go(c_x,c_y,x,y)
        if(w == 0):
            t.shape(mario_jump[0 if t_pos == 3 else 1])
            t.goto(x*size,y*size)
            t.penup()
            t.goto(x*size,y*size+size/2)
            time.sleep(0.01)
            t.goto(x*size,y*size)
            t.shape(mario[t_pos])
            t.pendown()
        elif(w != 2):
            t_pos = where_go(c_x,c_y,x,y)
            t.shape(mario[t_pos])
        time.sleep(0.1)
        t.goto(x*size,y*size)
        c_x, c_y = x,y
        time.sleep(0.1)
    t.color('red')
    t.pensize(5)
    t.clearstamp(s)
    visited.pop()
    for _ in range(10):
        t.shape(mario_king[0])
        time.sleep(0.01)
        t.shape(mario_king[1])
        time.sleep(0.01)
    #print(t_pos)
    t.shape(mario_king[1])
    while visited:
        x,y = visited.pop()
        w = where_go(c_x,c_y,x,y)
        if w == 0:
            t.shape(mario_king_jump[0 if t_pos == 3 else 1])
            t.goto(x*size,y*size)
            t.penup()
            t.goto(x*size,y*size+size/2)
            time.sleep(0.01)
            t.goto(x*size,y*size)
            t.shape(mario_king[1 if t_pos == 3 else 2])
            t.pendown()
        elif(w != 2):
            t_pos = where_go(c_x,c_y,x,y)
            t.shape(mario_king[1 if t_pos == 3 else 2])
        time.sleep(0.1)
        t.goto(x*size,y*size)
        c_x, c_y = x,y
        time.sleep(0.1)
        # print(k,t_pos)
        #time.sleep(0.1)
    turtle.mainloop()
