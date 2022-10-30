from copy import deepcopy
import random
visited = []
bfs_map = []
def BFS(maze_map,x,y):
    global visited,bfs_map

    

def makeMap()->list:
    maze_map= [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]
    wall_num = random.randint(10,30)
    print(wall_num)
    wall_list = [x for x in range(1,100)]
    random.shuffle(wall_list)
    for i in wall_list[:wall_num]:
        maze_map[i//10][i%10] = 1
    
    global visited,bfs_map
    for x in maze_map:
        print(x)
    print()
    bfs_map = deepcopy(maze_map)
    bfs_map[0][0] = 1
    visited = [(0,0)]
    que = [(0,0)]
    depth = 1
    while que:
        x,y = que.pop(0)
        depth =bfs_map[x][y] + 1
        if x>0 and (x-1,y) not in visited and maze_map[x-1][y] != 1:
            que.append((x-1,y))
            visited.append((x-1,y))
            bfs_map[x-1][y] = depth
        if y>0 and (x,y-1) not in visited and maze_map[x][y-1] != 1:
            que.append((x,y-1))
            visited.append((x,y-1))
            bfs_map[x][y-1] = depth
        if x<9 and (x+1,y) not in visited and maze_map[x+1][y] != 1:
            que.append((x+1,y))
            visited.append((x+1,y))
            bfs_map[x+1][y] = depth
        if y<9 and (x,y+1) not in visited and maze_map[x][y+1] != 1:
            que.append((x,y+1))
            visited.append((x,y+1))
            bfs_map[x][y+1] = depth
        #print('x',x,'y',y,'que:',que,'d',depth)
    m = depth-1 if depth < 11 else 10
    
    goal_list = []
    for i in range(10):
        for j in range(10):
            if bfs_map[i][j] >= m:
                goal_list.append((i,j))
    #print(m,goal_list)
    x,y = random.choice(goal_list)
    
    maze_map[x][y] = 2
    #print(bfs_map)

    # while True:
    #     x = random.randint(0,9)
    #     y = random.randint(0,9)
    #     if(maze_map[x][y]==0):
    #         maze_map[x][y] = 2
    #         break
    for x in range(10) :
        maze_map[x] = [1]+maze_map[x]+[1]
    
    maze_map = [[1 for _ in range(12)]] + maze_map + [[1 for _ in range(12)]]
    
    return maze_map
# for x in makeMap():
#     print(x)
