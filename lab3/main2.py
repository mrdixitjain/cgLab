from graphics import *
from graphicsCG import *
import math

def matMult(M, N):
	# print(M)
	# print(N)
	R=[]
	for i in range(len(M)):
		R.append([])
		for j in range(len(N[0])):
			R[i].append(0)
	for i in range(len(M)):
		for j in range(len(N[0])):
			for k in range(len(N)):
				R[i][j] += M[i][k] * N[k][j]
	for i in range(len(M)):
		for j in range(len(N)):
			M[i][j]=R[i][j]
	# print(M)
	return M[0]

def copyMetrics(M):
	a=[]
	for i in range(len(M)):
		a.append([])
		for j in M[i]:
			a[i].append(j)
		a[i].append(1)
	return a


def choices():
	print("select choice for transformation->")
	print("1. Translation")
	print("2. Scaling")
	print("3. Rotation")
	print("4. Shearing")
	print("5. Reflection")
	print("6. Quit")
	pass

if __name__=="__main__":	
	print("enter xmin, ymin, xmax, ymax for window: ", end="")
	xmin , xmax , ymin , ymax = map(int, input().split())
	window = size(xmin , xmax , ymin , ymax)

	print("enter xmin, ymin, xmax, ymax for viewPort: ", end="")
	xvmin , xvmax , yvmin , yvmax = map(int, input().split())
	viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

	win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin, autoflush = False)

	drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort )
	drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort )

	print("Enter number of edges of polygon: ", end="")
	n=int(input())
	print("Enter vertices of the edges as (x, y) one by one")
	vertices=[]
	for i in range(n):
		vertices.append(list(map(int, input().split())))
	print("Enter color of the Edges:- ", end="")
	color = input()
	drawPolygon(win, n, vertices, color, window, viewPort)
	choices()
	while(1):

		choice=int(input())

		if(choice==1): #translation
			print("enter Tx: ", end="")
			Tx=float(input())
			print("enter Ty: ", end="")
			Ty=float(input())

			T=[[1, 0, 0], [0, 1, 0], [Tx, Ty, 1]]
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				i=matMult([i], T)[:2]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)

		elif(choice==2): #Scaling
			print("enter Sx: ", end="")
			Sx=float(input())
			print("enter Sy: ", end="")
			Sy=float(input())

			S=[[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]]
			print("Reference point for rotation (x, y): ", end=" ")
			x, y = map(int, input().split())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				l=[i[0]-x, i[1]-y, i[2]]
				l=matMult([l], S)[:2]
				print(l)
				i[0]=x+l[0]
				i[1]=y+l[1]
				i=i[:2]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)

		elif(choice==3):
			print("enter angle of rotation: ", end="")
			angle=float(input())
			print("enter directon of rotation->")
			print("1. Anti Clockwise")
			print("2. Clockwise")
			k=int(input())
			if(k==2):
				angle=-angle
			R=[[math.cos(angle), math.sin(angle)], [-math.sin(angle), math.cos(angle)]]
			print("Reference point for rotation (x, y): ", end=" ")
			x, y = map(int, input().split())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				l=[i[0]-x, i[1]-y]
				l = matMult([l], R)
				i[0]=x+l[0]
				i[1]=y+l[1]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)


		elif(choice==4):
			print("enter shx: ", end="")
			shx=float(input())
			print("enter shy: ", end="")
			shy=float(input())
			Sh=[[1, shy, 0], [shx, 1, 0], [0, 0, 1]]
			print("Reference point for rotation (x, y): ", end=" ")
			x, y = map(int, input().split())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				l=[i[0]-x, i[1]-y, i[2]]
				l=matMult([l], Sh)[:2]
				print(l)
				i[0]=x+l[0]
				i[1]=y+l[1]
				i=i[:2]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)

		elif(choice==5):
			print("enter a, b, c where ax+by+c=0 is reference line: ", end="")
			a, b, c = map(float, input().split())

			k=copyMetrics(vertices)

			R = [[(b*b-a*a)/(a*a+b*b), -2*a*b/(a*a+b*b), 0],
				 [-2*a*b/(a*a+b*b), (a*a-b*b)/(a*a+b*b), 0],
				 [-2*a*c/(a*a+b*b), -2*b*c, 1]]

			for i in k:
				x=i[0]
				y=i[1]
				l=[x, y, 1]
				# i[0]=((b*b-a*a)*x-2*a*b*y-2*a*c)/(a*a+b*b)
				# i[1]=((a*a-b*b)*y-2*a*b*x-2*b*c)/(a*a+b*b)
				l=matMult([l], R)[:2]
				print(l)
				i[0]=math.ceil(l[0])
				i[1]=math.ceil(l[1])
				i=i[:2]
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)


		elif(choice==6):
			break

		else:
			pass
			print("please enter valid choice.")
		choices()



	print("Click on window to exit")


	win.getMouse()
	win.close 