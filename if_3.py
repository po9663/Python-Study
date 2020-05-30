num1,num2 = input("두 자리 정수 두개를 입력 : ").split()
num1 = int(num1)
num2 = int(num2)
x1 = num1//10
y1 = num1%10
x2 = num2//10
y2 = num2%10

if(x1==x2) and (y1==y2):
    print("두 정수는 모두 {}로 같은 정수입니다.".format(num1))

elif(x1==x2) and (not y1==y2):
    print("{},{}:하나의 숫자만 일치합니다.".format(num1,num2))
    
elif(not x1==x2) and (y1==y2):
    print("{},{}:하나의 숫자만 일치합니다.".format(num1,num2))

elif(not x1==x2) and (not y1==y2):
    if(x1 == y2) and (not x2 == y1):
        print("{},{}:하나의 숫자만 일치합니다.".format(num1,num2))
    elif(not x1==y2) and (x2==y1):
        print("{},{}:하나의 숫자만 일치합니다.".format(num1,num2))
    elif(x1 == y2) and (x2 ==y1):
        print("{},{}:자리 값만 다른 정수 입니다..".format(num1,num2))
    else :
        print("{},{}:일치하지 않는 정수입니다.".format(num1,num2))
