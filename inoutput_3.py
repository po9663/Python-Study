import math

x = input("두 점의 좌표값을 x1,y1,x2,y2 순서대로 입력 : ")
x1,y1,x2,y2 = x.split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

leng =  math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
print("두 점 사이의 거리는 %.2f 입니다"%leng)
if leng <= 5:
    print("두 점 사이의 거리는 5 이하 입니까? : {}".format('True'))
else :
    print("두 점 사이의 거리는 5 이하 입니까? : {}".format('False'))
    

