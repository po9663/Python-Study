employee = {'공유','고수','보검','태현','종민','세윤','준호','우종','시우','두준'}
late = {'우종','보검'}
absent = {'종민','우종','보검','두준'}
a = late.union(absent)
b = employee.difference(a)
print("전체 사원 명단 : {}".format(employee))
print("지각자 명단 : {}".format(late))
print("결근자 명단 : {}".format(absent))
print("보너스 지급 대상자 명단 : {}".format(b))
print("야근 대상자 명단 : {}".format(late))
c,d = input("신입사원 명단 입력 : ").split()
employee1 = {""}
employee1.add(c)
employee1.add(d)
if employee & employee1 :
    print("신입사원의 이름이 기존 사원의 이름과 중복")
employee.add(c)
employee.add(d)
print(employee)
