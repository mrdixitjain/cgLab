from graphics import *

win = GraphWin("line", 2000, 1000)


def f(x, y):
	return dy*x-dx*y+dx*y1-dy*x1

def positiveSlopeLine(x1, y1, x2, y2, d):
	print('in positiveSlopeLine')
	print(dx, dy)
	x=x1
	y=y1
	while(x<=x2):
		pt=Point(x, 999-y)
		pt.draw(win)
		if(f(x+1, y+1/2)<0):
			x=x+1
			d+=dy
		else:
			d+=dy-dx
			x+=1
			y+=1

def negativeSlopeLine(x1, y1, x2, y2, d):
	x=x1
	y=y1
	while(x<=x2):
		pt=Point(x, 999-y)
		pt.draw(win)
		if(f(x+1, y-1/2)<0):
			x=x+1
			y=y-1
			d+=dy+dx
		else:
			d+=dy
			x+=1

x1=int(input())
y1=int(input())
x2= int(input())
y2=int(input())#"enter y2: ""enter x2: ""enter y1: ""enter x1: "
if(x1>x2):
	x1, x2=x2, x1
	y1, y2=y2, y1
dx=x2-x1
dy=y2-y1
if(dx!=0):
	slope=dy/dx
else:
	slope='i'
d=2*dy-dx
if(slope>=0 or slope=='i'):
	positiveSlopeLine(x1, y1, x2, y2, d)
else:
	negativeSlopeLine(x1, y1, x2, y2, d)



win.getMouse()
win.close()