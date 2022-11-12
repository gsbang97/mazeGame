import turtle, time, math
from playsound import playsound
# 어느 방향으로 움직이는 지 반환하는 함수
# c_x,c_y : 현재 거북이의 위치
# x,y : 가야하는 좌표
# 1 : 왼쪽, 2: 아래, 3: 오른쪽, 4: 위
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
    # 이미지 경로
    mario_jump = ["./src/image/mario_jump.gif","./src/image/mario_jump2.gif"]
    mario_king_jump = ["./src/image/mario_king_jump.gif","./src/image/mario_king_jump2.gif"]
    mario_king = ["./src/image/mario_king1.gif","./src/image/mario_king2.gif","./src/image/mario_king3.gif"]
    mario = ["./src/image/mario_right.gif","./src/image/mario_left.gif"] # 1,3 -> 0,1
    mario_block = "./src/image/mario_block.gif"
    mario_mush = "./src/image/mario_mush.gif"
    mario_background = "./src/image/mario_background.gif"
    # 터틀그래픽의 이미지 설정 : 배경이미지와 일치시켰다.
    turtle.setup(width=800,height=500)
    t = turtle.Turtle()
    # 맵을 만드는 동안 펜이 그려지면 안된다. + 터틀이 보이면 안됨.
    t.penup()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    # 이미지 다 삽입해준다.
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
    # BGM ON
    playsound("./src/sound/BGM.wav",False)
    # play = multiprocessing.Process(target=playsound,args=("./src/sound/BGM.wav",))
    # play.start()

    # 맵 생성 -1: 벽, 2: 목적지
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
    
    # 토관에 들어가는 모션을 넣어준다. 
    t.shape(mario[0])
    t.color('blue')
    t.speed(3)
    t.goto(30,-215)
    t.showturtle()
    t.forward(180)
    # 토관 들어갈때 소리나게 하기
    playsound("./src/sound/pipe.wav",False)
    t.speed(1)
    t.forward(10)
    t.hideturtle()
    t.speed(10)
    # 토관에 들어간 뒤 마리오를 1,1 위치로 옮겨준다. (홈), 펜 색: blue(처음 탐색)
    t.goto(size,size)
    t.showturtle()
    # 이제부터 경로를 표시해야하므로 pendown 실행
    t.pendown()
    t.speed(1)
    t_pos = 0
    c_x, c_y = 1,1
    # 경로에서 x,y값을 하나씩 가져와서 그 값으로 움직이게 한다.
    for x,y in road:
        w = where_go(c_x,c_y,x,y)
        # 1 : 왼쪽, 2: 아래, 3: 오른쪽, 4: 위
        if(w == 3): # 점프(위)
            # 점프할때 소리나게 한다., 위로 올라갔다 나오는 모션을 보기 좋게 하기 위해 속도를 빠르게 움직이게 했다.
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
        elif(w != 2): # 아래로 가는게 아닌 경우 (점프도 자동으로 아님)
            t_pos = where_go(c_x,c_y,x,y) # 방향을 조정한다.
            t.shape(mario[t_pos%2])
        t.goto(x*size,y*size)
        c_x, c_y = x,y # 이동한 위치를 현재위치로 옮겨준다.
    # 목적지까지 갔으므로 다시 되돌아오는 경로는 빨간색으로 해준다. 
    # 좀더 잘 보이게 하기 위해 펜사이즈를 좀더 크게 해주었다.
    t.color('red')
    t.pensize(5)
    # 목적지 도착하면 해당 버섯을 제거함으로써 도착했다는 점을 명확하게 해준다.
    t.clearstamp(s)
    visited.pop()
    # 슈퍼마리오 변신 사운드 on
    playsound("./src/sound/power_up.wav",False)
    # 변신항때 커졌다 작아졌다 하는 모션
    for _ in range(10):
        t.shape(mario_king[0])
        time.sleep(0.01)
        t.shape(mario_king[1])
        time.sleep(0.01)
    t.shape(mario_king[1])
    # 집으로 돌아가는 경로 따라가기
    while visited:
        x,y = visited.pop()
        w = where_go(c_x,c_y,x,y)
        if w == 3: # 점프
            playsound("./src/sound/super_jump.wav",False)
            t.shape(mario_king_jump[t_pos%2])
            t.goto(x*size,y*size)
            t.penup()
            t.goto(x*size,y*size+size/2)
            t.goto(x*size,y*size)
            t.shape(mario_king[t_pos%2+1])
            t.pendown()
        elif(w != 2): # 점프, 아래 아닌 경우 : 방향이 전환될 수 있다. 그 외에는 방향이 안바뀜
            t_pos = where_go(c_x,c_y,x,y)
            t.shape(mario_king[t_pos%2+1])
        t.goto(x*size,y*size)
        c_x, c_y = x,y
    # 깃발 위치로 변경, 클리어 소리 재생
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
    # 자연스러운 점프를 위해 pi를 이용해 sin파처럼 움직이게 하기
    for i in range(0,140,10):
        p = math.pi * i/280
        t.goto(i/2-280,math.sin(p)*50-180)
    for i in range(0,140,10):
        p = math.pi * i/280
        t.goto(i/2-210,-130-math.sin(p)*85)
    t.speed(3)
    t.shape(mario_king[1])
    t.goto(-70,-215)
    turtle.mainloop()