num1,x,num2 = input("수식 입력(예:20*40) : ").split()
num1 = float(num1)
num2 = float(num2)
if x == '+':
    print("{:.6f} + {:.6f} = {:.6f}".format(num1,num2,num1+num2))
elif x == '-':
    print("{:.6f} - {:.6f} = {:.6f}".format(num1,num2,num1-num2))
elif x == '*':
    print("{:.6f} * {:.6f} = {:.6f}".format(num1,num2,num1*num2))
elif x == '/':
    if num2 == 0:
        print("{:.6f} 로 나누기를 수행할 수 없습니다.".format(num2))
    else : 
        print("{:.6f} / {:.6f} = {:.6f}".format(num1,num2,num1/num2))
else :
    print("{} 지원하지 않는 연산자 입니다.".format(x))
