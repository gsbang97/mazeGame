class node:
    up_link = None
    size = 0
    def __init__(self,x,y) -> None:
        self.pos = (x,y)
        pass
def makeRoad(maze_map) -> list:
    # x증가, y증가, x감소, y감소 방향 배열
    idx = ((1,0),(0,1),(-1,0),(0,-1))
    
    # 경로 
    road = [(1,1)]
    # 마리오 시점 맵
    mario_map = [
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-3,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,0,0,0,0,0,0,0,0,0,0,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    ]
    # 현재 위치 
    x,y = 1,1
    # 되돌아 갈때 사용하는 변수 
    flag = 0    
    # 방문한 위치
    # 목적지에 도착했는가?
    is_finish = False
    while not is_finish:
        cnt = 0
        # 좌 우 위 아래 중 1이 아닌 것들
        for i,j in idx:
            if maze_map[x+i][y+j] == -1:
                mario_map[x+i][y+j] = -1
            elif maze_map[x+i][y+j] == 0 and mario_map[x+i][y+j] != -3:
                mario_map[x+i][y+j] = -2
        # 상하좌우중 벽이 아니고 방문하지 않은 곳 
        d = [(x+i,y+j) for i,j in idx if (maze_map[x+i][y+j]) != -1 and (x+i,y+j) not in road ]
        if d:
            # 해당 값이 존재할 때 벽이 없는 곳
            # m_d = [[x+i,y+j] for i,j in idx if (maze_map[x+i][y+j]) != -1]
            # 상하 좌우 중 목적지가 있는경우 반복문 종료, 그리고, 상하좌우 중 길인 경우 -2 값을 넣는다 
            # 마리오 시점 -2: 방문하지 않은 길, -3: 방문한 길 , -1: 벽
            for i,j in d:
                if maze_map[i][j] == 2:
                    road.append((i,j))
                    mario_map[i][j] = -3
                    x,y = i,j
                    is_finish = True
                    break
                
            # 목적지 방문시 종료
            if(is_finish):
                break
            # d가 있다는 것은 되돌아가지 않고 현재위치에서 방문하지 않은 길이 있다는 것이다. 따라서 해당길로 움직이므로 되돌아가는 변수를 초기화시킨다.
            flag = 0
            # 마리오 맵에 해당 값 입력
            mario_map[d[0][0]][d[0][1]] = -3
            # 움직이기
            road.append(d[0])
            # 현재위치 초기화
            x,y = d[0]
        else:
            # 만약 주변이 이미 지나온 길 + 벽으로 막혀있는경우
            tmp_x, tmp_y = x,y
            while True:
                # 
                destination = None
                # 마리오 기준 주변에 이미 지나온 길 중에 그 사방에 돌아갈 길이 있다면
                for i,j in idx:
                    if mario_map[tmp_x+i][tmp_y+j] == -2:
                        for a,b in idx:
                            if mario_map[tmp_x+i+a][tmp_y+j+b] == 0:
                                destination = (tmp_x+i,tmp_y+j)
                                break
                if destination:
                    flag = 0
                    cnt+=1
                    des_x,des_y = destination
                    # 그 길로 돌아갈 수 있는 최단경로 찾기
                    root = node(x,y)
                    q = [root]
                    v = [(x,y)]
                    is_goal = True
                    n = None
                    while q and is_goal:
                        root = q.pop(0)
                        print("root",root)
                        c_x, c_y = root.pos
                        for i,j in [(c_x+n , c_y+m) for n,m in idx if (mario_map[c_x+n][c_y+m] < -1) and (c_x+n,c_y+m) not in v]:
                            v.append((i,j))    
                            n = node(i,j)
                            n.up_link = root
                            print("node\n",n)
                            q.append(n)
                            for i2,j2 in idx:
                                if maze_map[i2+i][j2+j] == 2:
                                    print("finish")
                                    root = n    
                                    n = node(i2+i,j2+j)
                                    n.up_link = root
                                    is_goal = False
                                    is_finish = True
                                    x,y = n.pos
                            if((i,j) == (des_x,des_y) and is_goal):
                                is_goal = False
                                break
                            if not is_goal:
                                break
                    q = []
                    print('n',n)
                    while n.up_link:
                        q.insert(0,n.pos)
                        mario_map[n.pos[0]][n.pos[1]] = -3
                        n = n.up_link
                    print('q',q)
                    road += q
                    if not is_finish:
                        x,y = destination
                    break
                else:
                    tmp_x,tmp_y = road[flag-2]
                    flag  = flag - 1       
    
    a,b = 1,1
    # 그 길로 돌아갈 수 있는 최단경로 찾기
    root = node(x,y)
    q = [root]
    v = [(x,y)]
    is_goal = True
    n = None
    cnt = 0
    while q and is_goal:
        root = q.pop(0)
        c_x, c_y = root.pos
        for i,j in [(c_x+n , c_y+m) for n,m in idx if (mario_map[c_x+n][c_y+m] == -3) and (c_x+n,c_y+m) not in v]:
            v.append((i,j))    
            n = node(i,j)
            n.up_link = root
            q.append(n)
            if((i,j) == (a,b)):
                is_goal = False
                break
    visited = []
    while n:
        visited.append(n.pos)
        n = n.up_link
    
    x,y = a,b          
    # for m in mario_map:
    #     print(m)
    return road, visited   
