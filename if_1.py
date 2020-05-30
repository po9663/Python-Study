num1,num2,num3 = input("세개의 정수를 입력하시오 : ").split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1>num2:
    if num2>num3:
        print("내림차순 정렬 : {} {} {}".format(num1,num2,num3))
    else :
        if num1>num3:
            print("내림차순 정렬 : {} {} {}".format(num1,num3,num2))
        else :
            print("내림차순 정렬 : {} {} {}".format(num3,num1,num2))
elif num1<num2:
    if num1>num3:
        print("내림차순 정렬 : {} {} {}".format(num2,num1,num3))
    else :
        if num2>num3:
            print("내림차순 정렬 : {} {} {}".format(num2,num3,num1))
        else :
            print("내림차순 정렬 : {} {} {}".format(num3,num2,num1))
