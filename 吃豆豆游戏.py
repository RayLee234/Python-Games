import random
from turtle import *
# 虚拟时间轴，用于记录当前时间
timer = 0
# 记录角色状态（收集到的豆豆数和血量）
state = { "score": 0, "blood": 3 }
# 记录角色位置和移动方向（及速度）
player = [15,-15]
direction = [6,0]
# 记录敌人数量、每一个敌人的位置、移动方向（及速度）和上一次造成角色减血的时间
enemyNum = 5
enemyPos = [ [105,195], [135,-165], [-135,165], [-225,45], [-315,-165] ]
enemyDir = [ [6,0], [-6,0], [0,6], [-6,0], [0,-6] ]
lastAttack = [ 0, 0, 0, 0, 0 ]
# 用于显示角色状态和生成游戏界面的小乌龟们
scoreWriter = Turtle(visible = False)
bloodWriter = Turtle(visible = False)
mapGenerator = Turtle(visible = False)
# 记录迷宫中每一个小正方形的属性：0表示墙壁小方块，1表示有豆豆的通道小方块，-1表示豆豆已经被吃掉的通道小方块
map = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
         0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
         0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0,
         0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
         0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
         0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1 ,0, 0, 1, 0,
         0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0,
         0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
         0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0,
         0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0,
         0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
         0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
         0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
         0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
         0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0,
         0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
         0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0,
         0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0,
         0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0,
         0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0,
         0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0,
         0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

# 用于每一时刻重新生成地下迷宫和豆豆
def generateMap():
    for i in range(len(map)):
        if map[i] != 0:
            x = i % 24 * 30 - 360
            y = 360 - i // 24 * 30 
            mapGenerator.up()
            mapGenerator.goto(x,y)
            mapGenerator.setheading(270)
            mapGenerator.color("green")
            mapGenerator.begin_fill()
            for dir in range(4):
                mapGenerator.forward(30)
                mapGenerator.left(90)
            mapGenerator.end_fill()
            if map[i] == 1:
                mapGenerator.goto(x+15,y-15)
                mapGenerator.dot(5,'goldenrod')

# 用于角色和敌人的移动、角色吃豆豆、角色掉血、维护血量和豆豆数
def move():
    global timer
    timer += 1 # timer加一，表示时间的推移
    # 更新角色状态
    scoreWriter.undo()
    scoreWriter.write(state['score'], font=('Arial',20,"normal"))
    bloodWriter.undo()
    bloodWriter.write(state['blood'], font=('Arial',20,"normal"))

    # 若血量为0，游戏结束
    if state['blood'] == 0:
        return
    
    # 重新生成地下迷宫和豆豆
    mapGenerator.clear()
    generateMap()

    clear()

    # 角色移动
    if valid(player[0]+direction[0], player[1]+direction[1]):
        player[0] += direction[0]
        player[1] += direction[1]
    up()
    goto(player[0],player[1])
    dot(30, 'yellow')

    # 若当前通道小方块中有豆豆，收集该豆豆
    curIndex = findIndex(player[0],player[1])
    if map[curIndex] == 1:
        map[curIndex] = -1
        state['score'] += 1

    # 敌人移动
    for i in range(enemyNum):
        if valid(enemyPos[i][0]+enemyDir[i][0], enemyPos[i][1]+enemyDir[i][1]):
            enemyPos[i][0] += enemyDir[i][0]
            enemyPos[i][1] += enemyDir[i][1]
        else:
            allDirections = [ [6,0], [-6,0], [0,6], [0,-6] ]
            newDirection = allDirections[random.randint(0,3)]
            enemyDir[i] = newDirection
        up()
        goto(enemyPos[i][0],enemyPos[i][1])
        dot(30, 'red')
    update()

    # 若角色离某个敌人过近，血量减一
    for i in range(enemyNum):
        if (enemyPos[i][0]-player[0]) ** 2 + (enemyPos[i][1]-player[1]) ** 2 <= 29 * 29:
            if timer - lastAttack[i] >= 12:
                state['blood'] -= 1
                lastAttack[i] = timer

    ontimer(move, 50)

# 用于计算坐标(x, y)在map中的第几个小方块内
def findIndex(x, y):
    return (x // 30 * 30 + 360) // 30 + 24 * (330 - (y // 30 * 30)) // 30

# 用于判断坐标(x, y)作为角色和敌人的位置是否合法
def valid(x, y):
    if map[findIndex(x-14, y)]==0 or map[findIndex(x+14, y)]==0:
        return False
    if map[findIndex(x, y-14)]==0 or map[findIndex(x, y+14)]==0:
        return False
    return abs(x) % 30 == 15 or abs(y) % 30 == 15

# 用于改变角色的移动方向
def changeDirection(x, y):
    if valid(player[0]+x, player[1]+y):
        direction[0], direction[1] = x, y

# 生成游戏界面
setup(800,800,400,0)
hideturtle()
tracer(False)
scoreWriter.up()
bloodWriter.up()
scoreWriter.goto(280,360)
scoreWriter.color('goldenrod')
scoreWriter.write('Score:', font=('Arial',20,"italic"))
scoreWriter.goto(350,360)
scoreWriter.write(state['score'], font=('Arial',20,"normal"))
bloodWriter.goto(280,340)
bloodWriter.color('red')
bloodWriter.write('Blood:', font=('Arial',20,"italic"))
bloodWriter.goto(350,340)
bloodWriter.write(state['blood'], font=('Arial',20,"normal"))
# 当玩家按下箭头键时，对应地改变主角的移动方向，不断调用move()函数
listen()
onkey(lambda: changeDirection(6, 0), 'Right')
onkey(lambda: changeDirection(0, 6), 'Up')
onkey(lambda: changeDirection(-6, 0), 'Left')
onkey(lambda: changeDirection(0, -6), 'Down')
move()

done()
