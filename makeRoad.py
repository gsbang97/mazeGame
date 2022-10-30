
from copy import deepcopy
import test,random
def makeRoad(maze_map) -> list:
    #maze_map = test.test_map1[:]

    # maze_map_test2 = test.test_map1[:]
    # maze_map_test = deepcopy(maze_map_test2)
    optimal_road = []
    road = [(1,1)]

    x,y = 1,1
    flag = 0
    print(maze_map)
    is_goal = maze_map[1][1] == 2
    t_pos = 1
    visited = [[1,1]]
    while not is_goal:
    #for tmp in range(30):
        # 좌 우 위 아래 중 1이 아닌 것들
        d = [[i,j] for i,j in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)] if (maze_map[i][j]) != 1 and [i,j] not in visited ]

        #random.shuffle(d)
        # print(d)
        # print("r",road[:][:2])
        # print("s",road[:][:])
        if d:

            # for x in d:
            #     x += [count(visited,x[:2])]
            # print("v",visited)
            # print("dd",d)
            #d.sort(key= lambda x: (x[3],abs(t_pos-x[2]),x[2]))
            # print(d)
            for i,j in d:
                if maze_map[i][j] == 2:
                    road.append((i,j))
                    visited.append([i,j])
                    is_goal = True
                    break
            if(is_goal):
                break
                
            flag = 0
            road.append(d[0][:2])
            visited.append(d[0][:2])
            x,y = d[0][:2]
        else:

            # print("xxxxx",x,y)
            # print(visited)
            if(len(road) > abs(flag-2)):
                x,y = road[flag-2][:2]
            else:
                x,y = 1,1
            road.append((x,y))
            flag = flag - 2
    cnt = 0
    return road, visited   
    # for i,j in road:
    #     cnt += 1
    #     if maze_map_test[i][j] == 0 or maze_map_test[i][j] == 2:
    #         maze_map_test[i][j] = str(cnt)
    #     else:
    #         maze_map_test[i][j] += " " +str(cnt)
    # cnt  =  0
    # while visited:
    #     x,y = visited.pop()
    #     d = [visited.index([i,j]) for i,j in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)] if [i,j] in visited ]
    #     if d:
    #         visited = visited[:min(d)+1]
    #     cnt += 1
    #     if maze_map_test2[x][y] == 0 or maze_map_test2[x][y] == 2:
    #         maze_map_test2[x][y] = str(cnt)
    #     else:
    #         maze_map_test2[x][y] += " " +str(cnt)
    #for i,j in visited[::-1]:
        

    # for i in range(12):
    #     for j in range(12):
    #         print(maze_map_test[i][j],end= "\t")
    #     print()
    # for i in range(12):
    #     for j in range(12):
    #         print(maze_map_test2[i][j],end= "\t")
    #     print()
    # #print(visited[::-1])
    # print(road)



#import numpy as np
#print(test.test_map)
# def count(list,inner):
#     cnt  = 0
#     for x in list:
#         if inner == x:
#             cnt +=1
#     return cnt

