# 绘制Python 

import turtle

def drawSnake(rad, angle, len, neckrad):
	for i in range(len):
		turtle.circle(rad,angle)
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	turtle.fd(rad)
	turtle.circle(neckrad+1,180)
	turtle.fd(rad*2/3)

def main():
	turtle.setup(1300,800,0,0)	#设置启动窗口的宽高和在屏幕的位置
	pythonsize = 30
	turtle.pensize(pythonsize)	#绘制大小
	turtle.pencolor("blue")	#颜色
	turtle.seth(-40)
	drawSnake(40,80,5,pythonsize/2)

main()
