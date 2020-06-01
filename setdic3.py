fruit = {'배' : [2, 1000], '자몽' : [1, 2000], '메론' : [1, 8000], '감' : [6, 800]}
fruit1 = input("먹고 싶은 과일은? : ")
if fruit1 in fruit :
    print(fruit1,"맛있게 드세요")
    fruit[fruit1][0] -= 1
else :
    print(fruit1,"준비되어 있지 않습니다")

values = list(fruit.values())
e = values[0][0]
f = values[1][0]
g = values[2][0]
h = values[3][0]
i = values[0][1]
j = values[1][1]
k = values[2][1]
l = values[3][1]
if e < 5:
    a = (5-e)*i
else :
    a = 0
if f < 5:
    b = (5-f)*j
else :
    b = 0
if g < 5:
    c = (5-g)*k
else :
    c = 0
if h < 5:
    d = (5-h)*l
else :
    d = 0
    
price = a+b+c+d
print("각 과일 당 최소 5개는 되도록 구입합니다")
print("구입에 필요한 총 금액은 {} 원 입니다".format(price))
