import random
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
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if(maze_map[x][y]==0):
            maze_map[x][y] = 2
            break
    for x in range(10) :
        maze_map[x] = [1]+maze_map[x]+[1]
    
    maze_map = [[1 for _ in range(12)]] + maze_map + [[1 for _ in range(12)]]
    
    return maze_map
