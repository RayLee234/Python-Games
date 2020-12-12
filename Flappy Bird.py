import random
from turtle import *
from collections import deque

writer = Turtle(visible = False)
# 用于统计分数
score = 0 # <------------------------------------------------------------------- line 7
# 用于记录角色的纵坐标
height = 0 # <------------------------------------------------------------------ line 9

# 两类障碍物及它们父类的定义，详见10.2继承一节中的讲解
class Object:
    def __init__(self):
        self.x = 400
    def inside(self):
        return self.x >= -400

class Ball(Object):
    def __init__(self):
        super().__init__()
        self.y = random.randint(-400, 400)
    def isTouching(self, xPos, yPos):
        return (xPos - self.x) ** 2 + (yPos - self.y) ** 2 <= 15 ** 2
    def draw(self):
        goto(self.x, self.y)
        dot(15, 'black')

class Pipe(Object):
    def __init__(self):
        super().__init__()
        self.y1 = random.randint(-300, 200)
        self.y2 = self.y1 + 100 # <-------------------------------------------- line 32
    def isTouching(self, xPos, yPos):
        return xPos>=self.x and xPos<=self.x+20 and (yPos<=self.y1 or yPos>=self.y2)
    def draw(self):
        goto(self.x, self.y1)
        setheading(270)
        begin_fill()
        forward(self.y1+400)
        left(90)
        forward(20)
        left(90)
        forward(self.y1+400)
        left(90)
        forward(20)
        end_fill()
        goto(self.x, self.y2)
        setheading(90)
        begin_fill()
        forward(400-self.y2)
        right(90)
        forward(20)
        right(90)
        forward(400-self.y2)
        right(90)
        forward(20)
        end_fill()

# 生成一个空队，用来存储角色当前时刻所有可见障碍物
obstacles = deque([])

def fly(x, y):
    global height
    height += 35

def generateObjects():
    clear()
    for obstacle in obstacles:
        obstacle.draw()
    goto(0, height)
    dot(15, 'green')

def move():
    global score, height # <--------------------------------------------------- line 74
    score += 1
    height -= 8
    writer.undo()
    writer.write(score, font=('Arial',30,"normal"))

    # 所有障碍物“后退”
    for obstacle in obstacles:
        obstacle.x -= 4 # <---------------------------------------------------- line 82

    # 每隔一段时间（当得分是100的倍数时）生成一个新管道类型障碍物
    if score % 100 == 0: # <--------------------------------------------------- line 85
        obstacles.append(Pipe())

    # 每隔一段时间（角色每次移动都有1/10的概率）生成一个新小球类型障碍物
    if random.randint(1,10) == 1: # <------------------------------------------ line 89
        if score % 100 > 5 or score % 100 < 95: # 防止小球在管道的开口处被生成
            obstacles.append(Ball())

    # 将队列开头超出屏幕范围的障碍物出队
    while len(obstacles) > 0 and not obstacles[0].inside():
        obstacles.popleft()

    # 重新生成角色、障碍物
    generateObjects()

    # 判断角色与屏幕边界、障碍物是否相碰
    if abs(height) > 400:
        writer.goto(-320,-20)
        writer.color('red')
        writer.write("Game Over", font=('Arial',120,"bold"))
        return
    for obstacle in obstacles:
        if obstacle.isTouching(0, height):
            writer.goto(-320,-20)
            writer.color('red')
            writer.write("Game Over", font=('Arial',120,"bold"))
            return
    ontimer(move, 50)

# 生成游戏界面
setup(800,800,400,0)
hideturtle()
tracer(False)
up()

# 书写当前得分
writer.up()
writer.goto(220,360)
writer.color('goldenrod')
writer.write('Score:', font=('Arial',30,"italic"))
writer.goto(310,360)
writer.write(score, font=('Arial',30,"normal"))

# 玩家点击屏幕时，调用fly()函数使角色高度增加
onscreenclick(fly)
move()
done()
