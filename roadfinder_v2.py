#from turtle import position
import test,random
#import numpy as np
#print(test.test_map)
def count(list,inner):
    cnt  = 0
    for x in list:
        if inner == x:
            cnt +=1
    return cnt

maze_map = deepcopy(test.test_map)
maze_map_test = deepcopy(test.test_map)
optimal_road = []
road = [(1,1,3)]

x,y = 1,1
flag = 0
print(maze_map)
is_goal = maze_map[1][1] == 2
t_pos = 1
visited = [[1,1]]
while not is_goal:
#for tmp in range(30):
    # 좌 우 위 아래 중 1이 아닌 것들
    d = [[i,j,k] for i,j,k in [(x+1,y,1),(x,y+1,2),(x-1,y,3),(x,y-1,4)] if (maze_map[i][j]) != 1 ]

    #random.shuffle(d)
    print(d)
    print("r",road[:][:2])
    print("s",road[:][:])
    if d:

        for x in d:
            x += [count(visited,x[:2])]
        print("v",visited)
        print("dd",d)
        #d.sort(key= lambda x: (x[3],abs(t_pos-x[2]),x[2]))
        print(d)
        for i,j,k,n in d:
            if maze_map[i][j] == 2:
                road.append((i,j,k))
                visited.append([i,j])
                is_goal = True
                break
        if(is_goal):
            break
            
        flag = 0
        road.append(d[0][:3])
        visited.append(d[0][:2])
        x,y,t_pos = d[0][:3]
    else:
        x,y = road[flag-1][:2]
        t_pos = 4 - road[flag-1][2]
        road.append((x,y,t_pos))
        flag = flag - 2
cnt = 0
for i,j,k in road:
    cnt += 1
    if maze_map_test[i][j] == 0 or maze_map_test[i][j] == 2:
        maze_map_test[i][j] = str(cnt)
    else:
        maze_map_test[i][j] += " " +str(cnt)
for i in range(12):
    for j in range(12):
        print(maze_map_test[i][j],end= "\t")
    print()
# for i,j in d:
#     print(maze_map[i][j])
# print(d)
import turtle
turtle_map = deepcopy(test.test_map)
t = turtle.Turtle()
t.penup()
for i in range(12):
    for j in range(12):
        goto(i*10,j*10)
        if(turtle_map[i][j] == 1):
            t.pendown()
            t.circle(3)
            t.penup()
turtle.exitonclick()
turtle.done()
# t.shape("turtle")
# t.right(90)
# t.forward(10)
# t.penup()
# t.pendown()
