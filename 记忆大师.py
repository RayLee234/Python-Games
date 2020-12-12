import random
from turtle import *

# 用于记录棋盘中每个小方格状态的变量
squares = list(range(32)) * 2
random.shuffle(squares)
remaining = [ True ] * 64
showing = [ False ] * 64

# 上一次有效点击的小方格下标和总点击次数
lastClick = -1
clicks = 0

writer = Turtle(visible = False)

# draw()函数用于根据小方格状态绘制每个小方格
def draw():
    clear()
    for i in range(64):
        up()
        if not remaining[i]:
            color('black', 'black')
        else:
            color('black', 'white')
        goto(findCorner(i))
        setheading(270)
        down()
        begin_fill()
        for dir in range(4):
            forward(80)
            left(90)
        end_fill()
        up()
        if remaining[i] and showing[i]:
            goto(findCenter(i))
            write(squares[i], font=('Arial',50,"bold"))

# findCenter()函数用于计算在序列中对应下标为index的小方格中显示数字的最佳位置
def findCenter(index):
    return index % 8 * 80 - 300, 250 - index // 8 * 80

# findCorner()函数用于计算在序列中对应下标为index的小方格左上角的横、纵坐标
def findCorner(index):
    return index % 8 * 80 - 320, 320 - index // 8 * 80

# findIndex()函数用于求出坐标(x, y)所在的小方格在序列中对应的下标
def findIndex(x, y):
    return int(320 - y) // 80 * 8 + int(x + 320) // 80

# click()函数用于实现玩家点击坐标位置(x, y)后的效果
def click(x, y):
    global clicks, lastClick, showing # global关键字的含义将在第十章中讲到
    if remaining.count(True) == 0 or clicks == 200:
        return
    if abs(x) > 320 or abs(y) > 320:
        return
    index = findIndex(x, y)
    if remaining[index] and not showing[index]:
        # 更新游戏界面上方显示的剩余点击次数
        writer.undo()
        writer.write(200 - clicks, font=('Arial',50,"bold"))

        clicks += 1 # 每次有效点击后更新总点击数
        if lastClick > 0 and squares[lastClick] == squares[index]:
            remaining[lastClick] = remaining[index] = False
        lastClick = index
        showing = [ False ] * 64
        showing[index] = True
    draw() # 更新棋盘状态后重新绘制棋盘
    
    # 判断游戏是否结束
    if remaining.count(True) == 0:
        writer.color('yellow')
        writer.goto(-305, -25)
        writer.write("You win! Congratulations!", font=('Arial',50,"bold"))
    elif clicks == 200:
        writer.color('red')
        writer.goto(-315, -20)
        writer.write("You lose : ) Good Luck next time!", font=('Arial',40,"bold"))

setup(800, 800, 400, 0)
hideturtle()
tracer(False)
# 在游戏界面上方显示出剩余点击次数
writer.up()
writer.goto(-298, 330)
writer.write('Number of clicks left: ', font=('Arial',50,"bold"))
writer.goto(222, 330)
writer.write(200 - clicks, font=('Arial',50,"bold"))
onscreenclick(click)
draw()
done()
