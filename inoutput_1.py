num1, num2, num3 = map(int,input("정수 숫자 3개를 입력 : ").split())
num4 = num1+num2+num3
num5 = (num4)/3
print("입력받은값 : {},{},{}".format(num1,num2,num3))
print("출력 : {}".format(num4))
print("평균 : {:1}".format(num5))
