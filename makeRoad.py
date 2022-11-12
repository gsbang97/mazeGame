class node:
    up_link = None
    size = 0
    def __init__(self,x,y) -> None:
        self.pos = (x,y)
        pass
    def __str__(self) -> str:
        s = "("+str(self.pos[0])+","+str(self.pos[1])+")"
        n = self.up_link
        while n:
            s += "("+str(n.pos[0])+","+str(n.pos[1])+")"
            n = n.up_link
        return s
def makeRoad(maze_map) -> list:
    # x증가, y증가, x감소, y감소 방향 배열
    idx = [(1,0),(0,1),(-1,0),(0,-1)]
    
    # 경로 
    road = [(1,1)]
    # 마리오 시점 맵
    mario_map = [[-1 for _ in range(12)]]+[[-1,0,0,0,0,0,0,0,0,0,0,-1] for _ in range(10)]+[[-1 for _ in range(12)]]
    mario_map[1][1] = -3
    # 현재 위치 
    x,y = 1,1
    # 되돌아 갈때 사용하는 변수 
    flag = 0    
    # 방문한 위치
    # 목적지에 도착했는가?
    is_finish = False
    while not is_finish:
        # 좌 우 위 아래 중 1이 아닌 것들
        for i,j in idx:
            if maze_map[x+i][y+j] == -1:
                mario_map[x+i][y+j] = -1
            elif maze_map[x+i][y+j] == 0 and mario_map[x+i][y+j] != -3:
                mario_map[x+i][y+j] = -2
        # 상하좌우중 벽이 아니고 방문하지 않은 곳 
        des_list = [(x+i,y+j) for i,j in idx if (maze_map[x+i][y+j]) != -1 and (x+i,y+j) not in road ]
        
        if des_list:
            # 해당 값이 존재할 때 벽이 없는 곳
            # 상하 좌우 중 목적지가 있는경우 반복문 종료, 그리고, 상하좌우 중 길인 경우 -2 값을 넣는다 
            # 마리오 시점 -2: 방문하지 않은 길, -3: 방문한 길 , -1: 벽
            for i,j in des_list:
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
            mario_map[des_list[0][0]][des_list[0][1]] = -3
            # 움직이기
            road.append(des_list[0])
            # 현재위치 초기화
            x,y = des_list[0]
        else:
            # 만약 주변이 이미 지나온 길 + 벽으로 막혀있는경우
            # 마리오 기준 주변에 이미 지나온 길 중에 그 사방에 돌아갈 길이 있다면 bfs 로 가장 가까운 미탐색 길을 탐색한다.
            # root 노드는 현재위치
            # 말단노드로 미탐색 길이 있는 곳을 찾으면 그 위치부터 부모노드를 따라가면서 경로를 저장한다.
            root = node(x,y)
            q = [root]
            v = [(x,y)]
            is_goal = True 
            n = None
            if(x,y) == (9,1):
                for m in mario_map:
                    print(m)
            while q and is_goal:
                root = q.pop(0)
                c_x, c_y = root.pos
                for i,j in [(c_x+n , c_y+m) for n,m in idx if (mario_map[c_x+n][c_y+m] != -1) and (c_x+n,c_y+m) not in v]:
                    v.append((i,j))    
                    n = node(i,j)
                    n.up_link = root
                    q.append(n)
                    for i2,j2 in idx:
                        if maze_map[i2+i][j2+j] == 2 :
                            root = n    
                            n = node(i2+i,j2+j)
                            n.up_link = root
                            is_goal = False
                            is_finish = True
                            break
                        elif mario_map[i2+i][j2+j] == 0:
                            is_goal = False
                            break
                    if not is_goal:
                        break
            q = []
            x,y = n.pos
            # 경로가 반대로 되어 있기 때문에 다시 되돌려준다.
            while n.up_link:
                q.insert(0,n.pos)
                t_x,t_y = n.pos
                mario_map[t_x][t_y] = -3
                for i,j in idx:
                    if mario_map[t_x+i][t_y+j] == 0:
                        mario_map[t_x+i][t_y+j] = -2 
                n = n.up_link
            road += q
                
    
    a,b = 1,1
    # 그 길로 돌아갈 수 있는 최단경로 찾기
    root = node(x,y)
    q = [root]
    v = [(x,y)]
    is_goal = True
    n = None
    # 위 알고리즘과 동일하게 bfs로 가장 먼저 길을 찾은 경롤로 다시 반환해준다.
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
    # print(road)
    # print(visited)  
    return road[1:], visited   