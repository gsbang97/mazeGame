from copy import deepcopy
import random    
def makeMap() -> list:
    d = 0
    while d<10:
        maze_map, d = makeMap_sub()
    return maze_map
# 랜덤으로 벽을 생성해 맵을 만든다. 
# 이때 생성되는 벽은 랜덤으로 지정되고, 시작지점에서 최단거리 10칸 이상인 곳에 지정하고,
# 그런곳이 존재하지 않으면 가장 먼 곳에 목적지로 지정한다.
# None -> map, 맵의 최대 깊이
def makeMap_sub() -> tuple[list,int]:
    # 초기 맵 데이터 모든 맵이 다 길이다.
    maze_map = [[0 for _ in range(10)] for _ in range(10)]
    wall_num = random.randint(10,30) # 벽의 개수 10~30개
    wall_list = random.sample(range(1,99),wall_num)
    # 벽은 -1로 지정
    for i in wall_list:
        maze_map[i//10][i%10] = -1
    # 맵을 deepcopy하여 해당 맵의 최대 깊이를 찾는다.
    bfs_map = deepcopy(maze_map)
    visited = [(0,0)]
    que = [(0,0)]
    depth = 0
    # BFS를 이용해, 모든 맵이 출발지점에서 얼마나 떨어져 있는지 저장한다.
    while que:
        x,y = que.pop(0)
        depth =bfs_map[x][y] + 1
        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= x+i <= 9  and 0<=y+j<=9 and (x+i,y+j) not in visited and maze_map[x+i][y+j] != -1:
                que.append((x+i,y+j))
                visited.append((x+i,y+j))
                bfs_map[x+i][y+j] = depth
    m = depth-1 if depth < 11 else 10

    # 모든 맵 중에서 가장 멀리 있는 곳 or 10보다 큰 위치를 모두 저장한 뒤에 랜덤으로 추출해 그 지점을 목적지로 지정한다.
    goal_list = []
    for i in range(10):
        goal_list.extend((i, j) for j in range(10) if bfs_map[i][j] >= m)
    x,y = random.choice(goal_list)
    maze_map[x][y] = 2
    # 맵 테두리에 벽 세우기
    for x in range(10) :
        maze_map[x] = [-1]+maze_map[x]+[-1]

    maze_map = [[-1 for _ in range(12)]] + maze_map + [[-1 for _ in range(12)]]

    return maze_map, depth
