month = ["January","February","March","April","May","Jun","July","August","September","October","Nobember","December"]
print("***** if조건문으로 작성 *****")
a = int(input("월을 입력하세요: "))
if a == 1:
    print("{}월은 January입니다".format(a))
elif a == 2:
    print("{}월은 February입니다".format(a))
elif a == 3:
    print("{}월은 March입니다".format(a))
elif a == 4:
    print("{}월은 April입니다".format(a))
elif a == 5:
    print("{}월은 May입니다".format(a))
elif a == 6:
    print("{}월은 Jun입니다".format(a))
elif a == 7:
    print("{}월은 July입니다".format(a))
elif a == 8:
    print("{}월은 August입니다".format(a))
elif a == 9:
    print("{}월은 September입니다".format(a))
elif a == 10:
    print("{}월은 October입니다".format(a))
elif a == 11:
    print("{}월은 Nobember입니다".format(a))
else :
    print("{}월은 December입니다".format(a))
print("***** 리스트로 작성 *****")
b = int(input("월을 입력하세요: "))
print("{}월은 {}입니다.".format(b,month[b-1]))
