import turtle, time, math
from playsound import playsound

def where_go(c_x,c_y,x,y)->int:
    if c_x - x == 1:
        return 1 
    elif c_y - y == 1:
        return 2
    elif c_x - x == -1:
        return 0
    else :
        return 3
def makeTurtle(size,road,visited,turtle_map)-> None:
    turtle.setup(width=800,height=500)
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    mario_jump = ["./src/image/mario_jump.gif","./src/image/mario_jump2.gif"]
    mario_king_jump = ["./src/image/mario_king_jump.gif","./src/image/mario_king_jump2.gif"]
    mario_king = ["./src/image/mario_king1.gif","./src/image/mario_king2.gif","./src/image/mario_king3.gif"]
    mario = ["./src/image/mario_right.gif","./src/image/mario_left.gif"] # 1,3 -> 0,1
    mario_block = "./src/image/mario_block.gif"
    mario_mush = "./src/image/mario_mush.gif"
    mario_background = "./src/image/mario_background.gif"
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
    screen.addshape(mario_background)
    screen.bgpic(mario_background)
    screen.title("마리오 미로찾기")
    playsound("./src/sound/BGM.wav",False)
    # play = multiprocessing.Process(target=playsound,args=("./src/sound/BGM.wav",))
    # play.start()

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
    
    t.shape(mario[0])
    t.goto(size,size)
    t.color('blue')
    t.speed(3)
    t.goto(30,-215)
    t.showturtle()
    t.forward(180)
    playsound("./src/sound/pipe.wav",False)
    t.speed(1)
    t.forward(10)
    t.hideturtle()
    t.speed(10)
    t.goto(20,20)
    t.showturtle()
    
    t.pendown()
    t.speed(1)
    t_pos = 0
    c_x, c_y = 1,1
    for x,y in road:
        w = where_go(c_x,c_y,x,y)
        if(w == 3):
            playsound("./src/sound/small_jump.wav",False)
            t.shape(mario_jump[t_pos%2])
            t.goto(x*size,y*size)
            t.penup()
            t.speed(3)
            t.goto(x*size,y*size+size/2)
            #time.sleep(0.01)
            t.goto(x*size,y*size)
            t.shape(mario[t_pos%2])
            t.speed(1)
            t.pendown()
        elif(w != 2):
            t_pos = where_go(c_x,c_y,x,y)
            t.shape(mario[t_pos%2])
        #time.sleep(0.1)
        t.goto(x*size,y*size)
        c_x, c_y = x,y
        #time.sleep(0.1)
    t.color('red')
    t.pensize(5)
    t.clearstamp(s)
    visited.pop()
    playsound("./src/sound/power_up.wav",False)
    for _ in range(10):
        t.shape(mario_king[0])
        time.sleep(0.01)
        t.shape(mario_king[1])
        time.sleep(0.01)
    t.shape(mario_king[1])
    
    while visited:
        x,y = visited.pop()
        w = where_go(c_x,c_y,x,y)
        if w == 3:
            playsound("./src/sound/super_jump.wav",False)
            t.shape(mario_king_jump[t_pos%2])
            t.goto(x*size,y*size)
            t.penup()
            t.goto(x*size,y*size+size/2)
            t.goto(x*size,y*size)
            t.shape(mario_king[t_pos%2+1])
            t.pendown()
        elif(w != 2):
            t_pos = where_go(c_x,c_y,x,y)
            t.shape(mario_king[t_pos%2+1])
        t.goto(x*size,y*size)
        c_x, c_y = x,y
    #play.terminate()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.shape(mario_king[2])
    t.goto(-280,140)
    playsound("./src/sound/clear.wav",False)
    
    t.showturtle()
    time.sleep(1)
    t.speed(3)
    t.goto(-280,-180)
    t.shape(mario_king_jump[0])
    t.speed(0)
    for i in range(0,140,10):
        p = math.pi * i/280
        #print(math.sin(p)*50-280,math.sin(p)*50-180, math.sin(i))
        t.goto(i/2-280,math.sin(p)*50-180)
    for i in range(0,140,10):
        p = math.pi * i/280
        #print(math.sin(p)*50-280,math.sin(p)*50-180, math.sin(i))
        t.goto(i/2-210,-130-math.sin(p)*85)
    # t.goto(-260,-140)
    # t.goto(-230,-130)
    #t.goto(-140,-215)
    t.speed(3)
    t.shape(mario_king[1])
    #t.speed(3)
    t.goto(-70,-215)
    turtle.mainloop()